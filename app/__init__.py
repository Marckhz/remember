from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

from flask_pymongo import PyMongo 
from flask_mail import Mail



import urllib.parse


username = urllib.parse.quote_plus('Scalzzi')
password = urllib.parse.quote_plus('metallica1')


app = Flask(__name__)

boostrap = Bootstrap()
csrf = CSRFProtect()
mail = Mail()



app.config["MONGO_URI"] = 'mongodb+srv://%s:%s@cluster0-csajn.gcp.mongodb.net/test?retryWrites=true' % (username, password)

mongo = PyMongo(app)

from app.views import page

def create_app(config):

	app.config.from_object(config)


	boostrap.init_app(app)
	csrf.init_app(app)
	mail.init_app(app)
	app.register_blueprint(page)

	return app