import os

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/p1dorsgang'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True  # Enable CSRF protection

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True