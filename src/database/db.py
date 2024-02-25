import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib import parse
from config.config import DB_HOST,DB_NAME,DB_PORT,DB_PWD,DB_USER
from sqlalchemy.engine.url import URL

print(DB_NAME,DB_USER,DB_PWD,DB_HOST)


POSTGRESSQL_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{parse.quote(DB_PWD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(POSTGRESSQL_DATABASE_URL)

engine = create_engine(POSTGRESSQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()