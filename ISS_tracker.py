import urllib2
import json
import geocoder
#pip install future
#pip install geocoder

response = urllib2.urlopen('http://api.open-notify.org/iss-now.json').read()
json_obj = str(response)

data = json.loads(json_obj)

time = data['timestamp']
timestamp = str(time)

position = data['iss_position']

longitude = position['longitude']
latitude = position['latitude']
print('The latitudial position of the ISS is currently: ' + latitude)
print('The longitudial position of the ISS is currently: ' + longitude )
print('Timestamp: ' + timestamp)



#http://www.geonames.org/export/web-services.html
#https://stackoverflow.com/questions/19590584/how-to-find-which-ocean-a-coordinate-is-on


g = geocoder.google([latitude, longitude], method='reverse')
#print(g.country_long)

g.city
g.state
g.state_long
g.country
g.country_long



###
geonames = urllib2.urlopen('http://api.geonames.org/findNearbyPlaceNameJSON?lat=47.3&lng=9&username=iMHx3RncHX').read()
_json_obj = str(geonames)

_data = json.loads(_json_obj)

geonamesData = _data['geonames']
