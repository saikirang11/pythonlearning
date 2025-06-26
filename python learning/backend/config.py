import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'devjwt')
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*') 