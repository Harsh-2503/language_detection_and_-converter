from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class CreateUserSchema(BaseModel):
    username: str
    password: str
    email: str


class UserAuthenticate(UserSchema):
    pass
