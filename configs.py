   
import os 

class Config(object):
    SECRET_KEY = os.urandom(32)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRESQL") + 'colegio'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    SECRET_KEY = 'development'
    SQLALCHEMY_ECHO = True

config_by_name = {
    'development': DevelopmentConfig
}