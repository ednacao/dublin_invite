"""Invite any customer within 100km of Dublin office (GPS coordinates 53.3381985, -6.2592576).

Output the names and user ids of matching customers (within 100 km), sorted by user id (ascending)."""

import json
import math

def load_file():
	for line in open("customers.txt"):
		line = line.strip()
		parts = line.split(',')
		latitude, user_id, name, longitude = parts
		print parts[3]

load_file()