
from flask import Blueprint
from flask import render_template, request, flash
from flask import request, jsonify

from . import mongo


from .email import welcome_email

from .forms import LoginForm
from .forms import RegisterForm




page = Blueprint('page', __name__)


@page.route("/")
def index():
	return "hello world"


@page.route('/register', methods = ['GET', 'POST'])
def register():

	form = RegisterForm(request.form)

	error = None
	
	name =  form.name.data
	profile= form.profil.data
	experience= form.experience.data
	focus_area= form.focus_area.data
	industry = form.industry.data

	if request.method == 'POST':

		datas = form.name.data
		mongo.db.users.insert_one({
			"name":name,
			"profile":profile,
			"experience":experience,
			"focus_area":focus_area,
			"industry":industry,

			})

	return render_template('register.html', title='Register', form = form)

@page.route('/login', methods = ['GET', 'POST'])
def login():

	form = LoginForm(request.form)
	error = None

	if request.method == 'POST':

		user = form.email.data

		query_user = {"email":user}

		#if mongo.db.users.find_one(query_user):
		#	error = "Email Already in Use"
		#else:
		mongo.db.users.insert_one({
				"email":user
				})
		
		welcome_email(user)

	flash(error)

	return render_template('index.html', title= 'Login', form = form)
