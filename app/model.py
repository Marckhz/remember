from werkzeug.security import check_password_hash


class User():

	def __init__(self, username):

		self.username = username

	def is_authenticated(self):

		return True

	def is_activate(self):

		return True


	def is_anonymous(self):
		return True


	def get_id(self):

		return  self.username

	@staticmethod
	def validate_login(email):
		return email