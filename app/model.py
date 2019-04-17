from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

	def __init__(self, email):

		self.email = email


	def is_authenticated():
		return True

	def is_active(self):
		return True

	def get_id(self):

		return self.email