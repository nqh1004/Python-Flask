import os

class Config:
    SECRET_KEY = 'e14cb4756d6223b64d2c7ef2b151d75d'
    SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')