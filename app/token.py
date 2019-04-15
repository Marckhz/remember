from itsdangerous import URLSafeTimedSerializer

from . import app


def generate_confirmation_email(email):

	signature = URLSafeTimedSerializer(app.config['SECRET_KEY'])

	return signature.dumps(email, salt = 'itsdangerous' )



def confirm_token(token, expiration = 3600):

	signature = URLSafeTimedSerializer(app.config['SECRET_KEY'])

	try:
		email = signature.loads(token, salt = 'itsdangerous', max_age = expiration)

	except:
		return False

	return email



