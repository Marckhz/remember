from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

boostrap = Bootstrap()
csrf = CSRFProtect()


from app.views import page

def create_app(config):

	app.config.from_object(config)


	boostrap.init_app(app)
	csrf.init_app(app)
	app.register_blueprint(page)

	with app.app_context():
		db.init_app(app)
		db.create_all()


	return app