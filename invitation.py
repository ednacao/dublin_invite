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


# latitude_dublin = 53.3381985
# longitude_dublin = -6.2592576

EARTH_RADIUS_KM = 6367

def spherical_law_of_cosines():
	central_angle = math.acos(
		(math.sin(latitude_dublin) * 
		math.sin(latitude_2)) + 
		(math.cos(latitude_dublin) * 
		math.cos(latitude_2)) * 
		(math.cos(longitude_2 - longitude_dublin))
	)

def great_circle_distance():
	return