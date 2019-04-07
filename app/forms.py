from wtforms import Form,validators
from wtforms import StringField
#from wtforms.validators import DataRequired


class LoginForm(Form):

	email = StringField('Email Address', [validators.Length(min=6, max = 50) ])
	

class RegisterForm(Form):

	name = StringField('Nombre', [ validators.Length(min=6, max=20) ])
	profil = StringField('Perfil', [validators.Length(min=6, max=20)])
	experience = StringField('Experiencia', [validators.Length(min=6, max=50)])
	focus_area = StringField('Area de Enfoque',[validators.Length(min=6, max=50)])
	industry = StringField('Industria',[validators.Length(min=6, max=50)])


