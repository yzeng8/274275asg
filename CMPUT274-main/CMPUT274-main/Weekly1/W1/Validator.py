def Validate(password):
	while True:
		if len(password) < 8:
			return "Invalid"
		if any (x in [" ", "#", "@"] for x in password):
			return "Invalid"
		if not (x.isupper() for x in password):
			return "Insecure"
		if not any(x.islower() for x in password):
			return "Insecure"
		if not any(x.isdigit() for x in password):
			return "Insecure"
		if not any(x in ['!', '-', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '_', '[', ']', '^', '`', '{', '|', '}', '~'] for x in password):
			return "Insecure"
		else:
			return "Secure"
pass

if __name__ == "__main__":
	print(Validate("passw0rd"))
	pass
