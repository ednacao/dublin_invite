"""Invite any customer within 100km of Dublin office (GPS coordinates 53.3381985, -6.2592576).

Output the names and user ids of matching customers (within 100 km), sorted by user id (ascending)."""

def load_file():
	my_file = open("customers.txt")
	print my_file.read()

load_file()