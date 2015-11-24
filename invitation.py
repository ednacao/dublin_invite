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
DUBLIN_LATITUDE = 53.3381985
DUBLIN_LONGITUDE = -6.2592576

latitude_2 = 52.986375
longitude_2 = -6.043701

def spherical_law_of_cosines():
	central_angle = math.acos(
		(math.sin(DUBLIN_LATITUDE) * 
		math.sin(latitude_2)) + 
		(math.cos(DUBLIN_LATITUDE) * 
		math.cos(latitude_2)) * 
		(math.cos(longitude_2 - DUBLIN_LONGITUDE))
	)

	arc_length = EARTH_RADIUS_KM * math.radians(central_angle)
	print arc_length


spherical_law_of_cosines()


