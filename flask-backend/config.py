from datetime import timedelta
from os import environ, path
from dotenv import load_dotenv

base_dir = path.dirname(__file__)
load_dotenv(path.join(path.dirname(base_dir), ".env"))

user = environ.get("POSTGRES_USER")
password = environ.get("POSTGRES_PASSWORD")
host = environ.get("POSTGRES_HOST")
port = environ.get("POSTGRES_PORT")
db = environ.get("POSTGRES_DB")

DB_URI = f"postgresql://{user}:{password}@{host}:{port}/{db}"

class Config:
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # ditambah
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_SECRET_KEY = "super-secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    