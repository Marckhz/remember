from flask_mail import Message
from flask import current_app, render_template, url_for


from .token import generate_confirmation_email, confirm_token


from . import mongo
from . import mail

def welcome_email(user):


	message = Message('Bienvenido a esta nueva pagina!' , sender = current_app.config['MAIL_USERNAME'],
						recipients = [user])

	token = generate_confirmation_email(user)

	
	confirm_url = url_for('page.confirm_email', token=token, _external = True)

	message.html = render_template('email/welcome.html', user=user, confirm_url = confirm_url)

	mail.send(message)