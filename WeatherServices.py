from pprint import pprint
import requests

city = input("What city are you in? ")
#print('CITY: ' + city )
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=5aaf03aa7fa904874c08c91d456f6d7b'
#pprint('URL is:   ' + url)
r = requests.get(url)
#pprint(r.json())
jsonData = r.json()
