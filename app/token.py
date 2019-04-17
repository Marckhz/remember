from itsdangerous import URLSafeTimedSerializer

from . import app
import random




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

def randomize(email):


	empty_list = []
	randoms = random.sample(range(10000), k = 60)
	z = ''.join(str(i) for i in randoms )
	psw = email + z
	encode = base64.b64encode(psw.encode('ascii'))
	#print(encode)
	
	#decode = base64.b64decode(encode).decode('ascii')
	
	return encode





