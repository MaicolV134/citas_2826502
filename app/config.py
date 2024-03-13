import os 
besadir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(besadir,  "database.db")
    SQLALCHEMY_TRACK_NOTIFICATIONS = True
    SECRET_KEY = "Michael"
    
    