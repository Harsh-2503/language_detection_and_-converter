from passlib.context import CryptContext
from jose import JWTError, jwt
from config.config import SECRET_KEY
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from src.database.models.user import User
from src.schemas.user import CreateUserSchema
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(plain_password):
    return pwd_context.hash(plain_password)


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: CreateUserSchema):
    # Check if user already exists
    if get_user(db, user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    user.password = hash_password(user.password)
    data = User(**user.dict())
    db.add(data)
    db.commit()
    return user


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return payload
