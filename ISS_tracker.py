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
#time related to position?


g = geocoder.google([latitude, longitude], method='reverse')
city = str(g.city)

if city == 'None':
    print('Over ocean. No data')
else:
    print(g.city)
    print(g.state_long)
    print(g.country_long)



###
#geonames = urllib2.urlopen('http://api.geonames.org/findNearbyPlaceNameJSON?lat=47.3&lng=9&username=iMHx3RncHX').read()
#DATA = json.loads(geonames)

#geonames2 = DATA['geonames']

#geonamesstr = str(geonames2)

#print(DATA['geonames']['countryName'])

#geonamesData = _data['geonames']

#print(geonamesData)
