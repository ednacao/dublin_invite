"""Invite any customer within 100km of Dublin office (GPS coordinates 53.3381985, -6.2592576).

Output the names and user ids of matching customers (within 100 km), sorted by user id (ascending)."""

import json
import math

for line in open("customers.json"):
	line = line.strip()
	parsed_json = json.loads(line)
	latitude = parsed_json['latitude']
	user_id = parsed_json['user_id']
	name = parsed_json['name']
	longitude = parsed_json['longitude']
	print latitude, user_id, name, longitude