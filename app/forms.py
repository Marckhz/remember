from wtforms import Form,validators
from wtforms import StringField, SelectField, FileField
from wtforms.widgets import TextArea

import re



class ProblemForm(Form):

	problem_description = StringField('Problem Description',[validators.Length(min=6, max = 1000000)], widget=TextArea() )
	industry = SelectField('Industry', 
									choices = [
												('Manufacturing', 'Manufacturing'), 
												('Medicine', 'Medicine'),
												('Education', 'Education'),
												('Food Services', 'Food Services'),
												('Financial', 'Financial') 
											])
	stage = SelectField('Stage',
								choices=[
										('Draft', 'Draft'),
										('Asking For Feedback', 'Asking For Feedback'),
										('On Review', 'On Review'),
										('Final', 'Final')
										])

	company = StringField('Company', [validators.Length(min=6, max=5000) ])
	company_tagline = StringField('Company Tagline', [validators.Length(min=6, max = 50000) ])
	ceo = StringField('Ceo', [validators.Length(min=6, max= 50) ])



class LoginForm(Form):

	email = StringField('Email Address', [validators.Length(min=6, max = 50) ])
	password = StringField('password', [validators.Length(min=6, max = 50)])
	

class RegisterForm(Form):



	email = StringField('Email', [validators.Length(min=6, max=50) ])
	name = StringField('Nombre', [ validators.Length(min=6, max=20) ])
	profil = StringField('Perfil', [validators.Length(min=6, max=20)])
	experience = StringField('Experiencia', [validators.Length(min=6, max=50)])
	focus_area = StringField('Area de Enfoque',[validators.Length(min=6, max=50)])
	industry = StringField('Industria',[validators.Length(min=6, max=50)])


class TokenForm(Form):

	token_form = StringField('Token', [ validators.Length(min=6, max=20) ])
