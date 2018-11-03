from pprint import pprint
import requests
from visual_recognition_v3 import visRec

# Categories for the articles of clothing
tops = ["tshirts", "tanktops", "blouses", "polos", "sweaters", "longsleeves"]
outerwear = ["hoodies", "denimjacket", "bomberjackets", "regularjackets"]
bottoms = ["skirts", "denimshorts", "shorts", "regularpants", "jeans"]
dresses = ["dresses"]

city = input("What city are you in? ")

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=5aaf03aa7fa904874c08c91d456f6d7b'
r = requests.get(url)
jsonData = r.json()

maxKelvin = jsonData['main']['temp_max']
minKelvin = jsonData['main']['temp_min']
windMPH = jsonData['wind']['speed']

# pprint(jsonData)

def KelvinToFaren(K):
    return (9/5) * (K - 273) + 32

maxTemp = KelvinToFaren(maxKelvin)
minTemp = KelvinToFaren(minKelvin)

# Determines which articles of clothing we will restrict
def restrictOutfits(maxTemp, minTemp, windMPH):
    clothes = visRec()
    filteredOptions = []
    if windMPH > 1:
        for i in clothes:
            for j in i:
                if i.get(j) != "skirts" and i.get(j) != "dresses":
                    filteredOptions.append(i)
        clothes = filteredOptions
        filteredOptions = []
    if maxTemp > 85:
        f = lambda x: x[1] == "denimshorts" or x[1] == "shorts" or x[1] == "tshirts" or x[1] == "polos" or x[1] == "skirts" or x[1] == "dresses"
    elif minTemp > 70:
        f = lambda x: x[1] != "denimjacket" and x[1] != "bomberjackets" and x[1] != "hoodies" and x[1] != "regularjackets"
    else:
        f = lambda x: x[1] != "skirts" and x[1] != "dresses" and x[1] != "shorts" and x[1] != "tanktops" and x[1] != "denimshorts"
    for c in clothes:
        filteredOptions.extend(list(filter(f, c.items())))
    return filteredOptions

def pairOutfits():
    outfits = restrictOutfits(maxTemp, minTemp, windMPH)
    print(maxTemp)
    print(minTemp)
    print(windMPH)
    for c in outfits:
        print(c)

pairOutfits()
