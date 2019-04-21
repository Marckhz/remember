
from flask import Blueprint
from flask import render_template, request, flash, session, redirect,url_for
from flask import request, jsonify

from pymongo import ReturnDocument

from . import mongo
from . import mail

import os
from io import BytesIO


import re
import pprint

from flask_login import login_required, login_user

from . import login_manager


from .email import welcome_email

from .token import generate_confirmation_email, confirm_token, randomize

from .forms import LoginForm
from .forms import RegisterForm
from .forms import TokenForm
from .forms import ProblemForm
from .forms import SearchBar
from .forms import ImageForm

from .model import User

import base64
from  PIL import Image




page = Blueprint('page', __name__)


@login_manager.user_loader
def load_user(user_id):
  mongo_user = mongo.db.users.find_one({"email":user_id })
  return User(user_id)


@page.route('/', methods =['GET', 'POST'])
def index():

  form = LoginForm()

  query = mongo.db.problems.find({})

  return render_template('home.html', form = form, query = query)


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
        print(instance_user.email)
        flash('Hemos enviado un link para su inicio de sesion', 'success') 

    if find_user is None:
      mongo.db.users.insert_one({"email":form.email.data})
      flash('Lo estamos redireccionando para completar su registro', 'primary')
      return redirect(url_for('page.register'))

  return render_template('layout.html', title= 'Login', form = form)


@page.route('/add_a_problem', methods = ['GET', 'POST'])
def add_problem():

  problemForm = ProblemForm(request.form )
  form = LoginForm()
  if request.method == 'POST':  
    file = request.files['file']
    file_to_b64 = base64.b64encode(file.read() )

    #falta un campo de descripcion
    find_user = mongo.db.problems.insert({"email":session['username'],
                    "problemName":problemForm.problem_description.data,
                    "industry":problemForm.industry.data,
                    "stage":problemForm.stage.data,
                    "company":problemForm.company.data,
                    "company_tagline":problemForm.company_tagline.data,
                    "image":file_to_b64.decode("utf-8")
              
              })
    print(file_to_b64)
  return render_template('add_problem.html', title='add problem', form=form, problemForm= problemForm)

@page.route('/all_problems', methods = ['GET'])
def all_problem():
  
  database = mongo.db.users.find({})

  return render_template('all_problem.html', title='all problem', database=database)



@page.route('/problem_description/<problem>')
def get_problem(problem):

  for index in mongo.db.users.find({}):
    email = index['email']
    for item in index['added_problems']:
      problem = item['problemName']
      industry = item['industry']
      stage = item['stage']

  return render_template('show.html', problem=problem, email = email, industry=industry, stage=stage, title='show')




