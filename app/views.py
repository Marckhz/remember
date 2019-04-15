
from flask import Blueprint
from flask import render_template, request, flash, session, redirect,url_for
from flask import request, jsonify

from . import mongo
from . import mail


#from flask_login import LoginManager

from flask_login import login_required, login_user, login_manager

from . import LoginManager


from .email import welcome_email

from .token import generate_confirmation_email, confirm_token

from .forms import LoginForm
from .forms import RegisterForm
from .forms import TokenForm


from .model import User



page = Blueprint('page', __name__)




@page.route("/")
def index():
	return "hello world"


@page.route('/hello')
def hello():

	return render_template('landing.html', title = 'yay')


@page.route('/auth/<token>')
def confirm_email(token):
	try:
		email = confirm_token(token)
		
	except:
		flash('error')
	return redirect(url_for('page.hello'))

@page.route('/register', methods = ['GET', 'POST'])
def register():

	form = RegisterForm(request.form)

	error = None
	
	name =  form.name.data
	profile= form.profil.data
	experience= form.experience.data
	focus_area= form.focus_area.data
	industry = form.industry.data

	if 'email' in session:

		if request.method == 'POST':

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

		find_user = mongo.db.users.find({"email":user})

		if user in find_user:			
			welcome_email(user)
			if user and User.validate_login(find_user['email']):
				user_obj = User(user['email'])
				login_user(user_obj)
				return redirect(url_for('hello'))
		else:
			mongo.db.users.insert_one({
					"email":user
					})
			welcome_email(user)

	return render_template('index.html', title= 'Login', form = form)
