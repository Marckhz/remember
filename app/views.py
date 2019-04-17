
from flask import Blueprint
from flask import render_template, request, flash, session, redirect,url_for
from flask import request, jsonify

from pymongo import ReturnDocument

from . import mongo
from . import mail


import re
import pprint

#from flask_login import LoginManager

from flask_login import login_required, login_user

from . import login_manager


from .email import welcome_email

from .token import generate_confirmation_email, confirm_token, randomize

from .forms import LoginForm
from .forms import RegisterForm
from .forms import TokenForm
from .forms import ProblemForm


from .model import User

import base64


page = Blueprint('page', __name__)


@login_manager.user_loader
def load_user(user_id):
  mongo_user = mongo.db.users.find_one({"email":user_id })
  return User(user_id)


@page.route("/")
def index():
	return "hello world"


@page.route('/hello')
@login_required
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
@login_required
def register():

	form = RegisterForm(request.form)

	error = None
	find_user = None

	print(session['username'])
	if request.method == 'POST':
		update_profile = mongo.db.users.find_one_and_update({"email":session['username']}, 
																{"$set": {"profile":
																			[{
																				'name':form.name.data,
                                        'profile':form.profil.data,
                                        'experience':form.experience.data,
                                        'focus_area':form.focus_area.data,
                                        'industry':form.industry.data
																			}] 
																		}
															})													

		flash("Yay Hemos actualizado tu perfil, de momento enviaremos un email para que puedas ingresar (: ")
		welcome_email(session['username'])


	return render_template('register.html', title='Register', form = form)


@page.route('/login', methods = ['GET', 'POST'])
def login():


  form = LoginForm(request.form)
  find_user = None

  if request.method == 'POST':
    find_user = mongo.db.users.find_one({"email":form.email.data})
    if find_user is not None:
      instance_user = User(find_user['email'])
      if instance_user.email == find_user['email']:
        welcome_email(instance_user.email)
        login_user(instance_user)
        session['username'] = instance_user.email
        flash('Hemos enviado un link para su inicio de sesion') 

    if find_user is None:
      mongo.db.users.insert_one({"email":form.email.data})
      flash('Lo estamos redireccionando para completar su registro')
      return redirect(url_for('page.register'))

  return render_template('index.html', title= 'Login', form = form)


@page.route('/add_a_problem', methods = ['GET', 'POST'])
def add_problem():
	
	form = ProblemForm(request.form)

	if request.method == 'POST':
		find_user = mongo.db.users.find_one_and_update({"email":session['username']},
                                                    {"$set":{"added_problems":
                                                          [{
                                                            "problemName":form.problem_description.data,
                                                            "industry":form.industry.data,
                                                            "stage":form.stage.data,
                                                            "company":form.company.data,
                                                            "company_tagline":form.company_tagline.data,
                                                            "ceo":form.ceo.data
                                                          }]
                                                    } }
                                                  )


	return render_template('add_problem.html', title='add a problem', form = form)


@page.route('/all_problems', methods = ['GET'])
def all_problem():
  
  database = mongo.db.users.find({})

  return render_template('all_problem.html', title='all problem', database=database)