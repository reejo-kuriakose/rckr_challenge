from math import radians, cos, sin, asin, sqrt
import requests

json_data = requests.get('https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json')
country_data = json_data.json()
radius = 6371

def has_exclusive_currency(currency):
    count = 0
    for country in country_data:
        if(country['currencies'][0] == currency):
            count = count + 1
    if(count > 1):
         return 0
    else:
         return 1

def distance(lat1, lat2, lon1, lon2):
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * asin(sqrt(a))
	return(c * radius)

pop_limit = int(input("Enter the population limit: "))

top_20 = []

for country in country_data:
     if(country['population'] >= pop_limit and has_exclusive_currency(country['currencies'][0])):
        top_20.append(country)

top_20 = sorted(top_20, key=lambda x: x['population'], reverse=False)

top_20 = top_20[:20]

distance_sum = 0.0
while top_20:
    country = top_20.pop(0)
    for val in top_20:
        distance_sum = distance_sum + distance(country['latlng'][0], (val['latlng'][0]), country['latlng'][1], val['latlng'][1])

print (round(distance_sum, 2))
