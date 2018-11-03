from pprint import pprint
import requests

city = input("What city are you in? ")

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=5aaf03aa7fa904874c08c91d456f6d7b'
r = requests.get(url)
jsonData = r.json()

maxKelvin = jsonData['main']['temp_max']
minKelvin = jsonData['main']['temp_min']

def KelvinToFaren(K):
    return (9/5) * (K - 273) + 32

maxTemp = KelvinToFaren(maxKelvin)
minTemp = KelvinToFaren(minKelvin)
