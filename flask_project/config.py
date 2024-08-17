import os

DB_USERNAME = 'root'
DB_PASSWORD = 'Letmesee12345@'
DB_HOST = 'localhost'
DB_NAME = 'bms'

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False