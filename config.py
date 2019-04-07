#from app import create_app

class Config:

	pass


class DevelopmentConfig(Config):


	DEBUG = True


	
config = {
	
		  'development':DevelopmentConfig,
		  'defualt':DevelopmentConfig,

	}