import os
class Config:
    SECRET_KEY='4d07c0e3a303992bfd4adfd200b33f89'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER= 'smtp.office365.com'
    MAIL_PORT=587
    MAIL_USE_TLS= True
    MAIL_USE_SSL= False
    MAIL_USERNAME=os.environ.get('EMAIL_USER')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
   