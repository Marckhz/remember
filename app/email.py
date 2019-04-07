from flask_mail import Message
from flask import current_app, render_template

import token_generator

from . import mail

def welcome_email(user):


	toke = token_generator()

	message = Message('Bienvenido a esta nueva pagina!' , sender = current_app.config['MAIL_USERNAME'],
						recipients = [user])

	message.html = render_template('email/welcome.html', user=user)
	mail.send(message)