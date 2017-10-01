
import urllib.request
import json

response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json').read()
json_obj = str(response, 'utf-8')

data = json.loads(json_obj)

time = data['timestamp']
timestamp = str(time)

position = data['iss_position']

longitude = position['longitude']
latitude = position['latitude']
print('The longitudial position of the ISS is currently: ' + longitude )
print('The longitudial position of the ISS is currently: ' + latitude)
print('Timestamp: ' + timestamp)
