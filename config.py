import os

class Config:
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')  
    DB_PORT = os.getenv('DB_PORT', '5432') 
    DB_NAME = os.getenv('DB_NAME', 'db')
    
    # need to check this sqlachemy uri for posgres
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
