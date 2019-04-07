from app import create_app
from flask_script import Manager
from config import config
from flask_pymongo import PyMongo 


config_class = config['development']

app = create_app(config_class)
app.config['MONGO_URI'] = "mongodb://localhost:27017/remember"
mongo = PyMongo(app)



if __name__ == '__main__':
	manager = Manager(app)
	manager.run()
