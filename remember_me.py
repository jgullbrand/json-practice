#Load the username if it has been stored previously.
#Otherwise, prompt for the username and store it in a new json file.

import json

json_file = "username.json"

def get_stored_username():
	"""check to see if username has been created"""
	filename = json_file
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None		
	else:
		return username

def get_new_username():
	"""prompt for new username"""
	username = input ("What is your name? ")
	filename = json_file
	with open (filename, "w") as file_object:
		json.dump(username,file_object)
	return username

def greet_user():
	"""Greet user by name"""
	username = get_stored_username()
	if username:
		check_username = input("is {} the correct username? (yes/no) \n> ".format(username))
		if check_username.lower() == "yes":
			print("Welcome back {}.".format(username))
		elif check_username.lower() == "no":
			get_new_username()	
			print("We'll remember you when you're back!")
		else:
			print("Please select yes or no.")	
	else:
		username = get_new_username()
		print("We'll remember you when you're back!")		

greet_user()


