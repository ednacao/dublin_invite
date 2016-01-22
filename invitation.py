"""Invite any customer within 100km of Dublin office (GPS coordinates 53.3381985, -6.2592576).

Output the names and user ids of matching customers (within 100 km), sorted by user id (ascending)."""

import sys
import json
import math

def calculate_arc_length(latitude,longitude):
	# Constants
	EARTH_RADIUS_KM = 6367
	DUBLIN_LATITUDE = 53.3381985
	DUBLIN_LONGITUDE = -6.2592576

	# Spherical Law of Cosines
	central_angle = math.acos(
					(math.sin(DUBLIN_LATITUDE) * 
					math.sin(latitude)) + 
					(math.cos(DUBLIN_LATITUDE) * 
					math.cos(latitude)) * 
					(math.cos(longitude - DUBLIN_LONGITUDE))
					)

	return EARTH_RADIUS_KM * math.radians(central_angle)


def process_file():
	near_dublin_dict = {}
	# Load in file and parse values
	f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin    
	for line in f:
		line = line.strip()
		parsed_json = json.loads(line)

		latitude = float(parsed_json['latitude'])
		user_id = int(parsed_json['user_id'])
		name = parsed_json['name']
		longitude = float(parsed_json['longitude'])

		arc_length = calculate_arc_length(latitude, longitude)

		if arc_length < 100:
			near_dublin_dict[user_id] = name


	for item in sorted(near_dublin_dict.keys()):
		print "ID:", item, "Name:", near_dublin_dict[item]


process_file()
