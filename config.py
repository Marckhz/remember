#from app import create_app
from flask_pymongo import PyMongo 


class Config:
	
	SECRET_KEY = 'pixelmarco'


class DevelopmentConfig(Config):
	
	DEBUG = True
	#SQLALCHEMY_DATABASE_URI  = 'mysql://marco:metallica1@localhost:3333/remember'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'marcohdes94i@gmail.com'
	MAIL_PASSWORD = 'metallica_1_h94'

	
config = {
	
		  'development':DevelopmentConfig,
		  'default':DevelopmentConfig,

	}