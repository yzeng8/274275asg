def validate(password):
	while True:
		if len(password) < 8: #If the password is less than 8 word, invalid
			return "Invalid"
		if any (x in [" ", "#", "@"] for x in password): #if password contains these characters, it is invalId
			return "Invalid"
		if not any(x.isupper() for x in password): #if password does not contain a uppercaSe character, insecure
			return "Insecure"
		if not any(x.islower() for x in password): #if password does not contain a lowercase character, insecure
			return "Insecure"
		if not any(x.isdigit() for x in password): #if password does not contain a number from 0 to 9, insecure
			return "Insecure"
		if not any(x in ['!', '-', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '_', '[', ']', '^', '`', '{', '|', '}', '~'] for x in password):
			return "Insecure" #if password does not contain a special character, insecure
		else:
			return "Secure" #if password pass all the tests, a Secure passWord!!!
pass

def generate(n):
	digit = random(string.digits)
	LC = random(string.ascii_letters)
	UC = upper(random(string.ascii_letters))
	SC = ['!', '-', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '_', '[', ']', '^', '`', '{', '|', '}', '~']
	password = digit + LC + UC + SC
	print(password)
	pass

if __name__ == "__main__":
	print(validate()) #Password input
	pass
