import os
from dotenv import load_dotenv

load_dotenv()

openAiKey = os.environ.get("OPENAI_API_KEY")

DB_USER = os.environ.get("DB_USER")
DB_PWD = os.environ.get("DB_PWD")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
SECRET_KEY = os.environ.get("SECRET_KEY")
