"""Invite any customer within 100km of Dublin office (GPS coordinates 53.3381985, -6.2592576).

Output the names and user ids of matching customers (within 100 km), sorted by user id (ascending)."""

import json
import math


# Constants
EARTH_RADIUS_KM = 6367
DUBLIN_LATITUDE = 53.3381985
DUBLIN_LONGITUDE = -6.2592576


def calculate_arc_length():
	# Load in file and parse values
	for line in open("customers.json"):
		line = line.strip() # <type str>
		parsed_json = json.loads(line) # <type dict>

		latitude = float(parsed_json['latitude'])
		user_id = str(parsed_json['user_id'])
		name = parsed_json['name']
		longitude = float(parsed_json['longitude'])

		# Spherical Law of Cosines
		central_angle = math.acos(
		(math.sin(DUBLIN_LATITUDE) * 
		math.sin(latitude)) + 
		(math.cos(DUBLIN_LATITUDE) * 
		math.cos(latitude)) * 
		(math.cos(longitude - DUBLIN_LONGITUDE))
		)

		arc_length = EARTH_RADIUS_KM * math.radians(central_angle)

		if arc_length < 100:
			print "ID:",user_id,name,"Arc length:",arc_length


calculate_arc_length()

