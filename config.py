import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:FirstDevWork@localhost:5432/flask_auth_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key-change-this"