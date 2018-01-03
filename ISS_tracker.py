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
    print('ISS is over ' + g.state_long + ', ' + g.country_long + 'and the nearest city is ' + g.city)
