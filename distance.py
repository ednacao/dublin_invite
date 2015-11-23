import math

latitude_dublin = 53.3381985
longitude_dublin = -6.2592576

latitude_2 = 52.986375
longitude_2 = -6.043701


great_circle_result = math.acos(math.sin(latitude_dublin*latitude_2)
	+ math.cos(latitude_dublin*latitude_2)
	* math.cos(longitude_2-longitude_dublin)
	)

distance_between_points = 6371 * math.radians(great_circle_result)

#  function for great-circle formula
## take arccos of:
## sin of first latitude times sin of second latitude
## then add cos of first latitude times cos second latitude
## times cos second longitude minus first longitude
## THEN:
## distance = radius of earth times value above

####
# arccos(sin1sin2 + cos1cos2cos(longitude1-longitude2))
###

print great_circle_result
print distance_between_points