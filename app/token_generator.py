import random
import string


def token_generator():


	random_numbers = random.randrange(0, 100000)
	letters = string.ascii_letters
	token = []
	choice_from_letters = random.choices(letters, k=5)

	for letter in choice_from_letters:
		token.append(letter)
	token.append(str(random_numbers))

	unify = ''.join(token)
	
	return unify
