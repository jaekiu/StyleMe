from pprint import pprint
import requests
from visual_recognition_v3 import visRec

# Categories for the articles of clothing
tops = ["tshirts", "tank tops", "blouses", "polos", "sweaters", "longsleeves"]
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
    print("Hmm, let me think...")
    clothes = visRec()
    filteredOptions = []
    if windMPH > 1:
        for i in clothes:
            for j in i:
                if i.get(j) != "skirts" and i.get(j) != "dresses":
                    filteredOptions.append(i)
        clothes = filteredOptions
        filteredOptions = []
    print("Finding good clothes to wear given today's details...")
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
    print("Combining clothes in new and interesting ways...")
    matchedOutfits = []

    for o in outfits:
        if o[1] == 'dresses':
            matchedOutfits.append([o[0]])
        elif o[1] in bottoms:
            for t in [y[0] for y in outfits if y[1] in tops]:
                matchedOutfits.append([o[0], t])


    print("Checking out your jacket collection...")
    temp = []
    for outer in [o for o in outfits if o[1] in outerwear]:
        for other in matchedOutfits:
            temp2 = other[:]
            temp2.append(outer[0])
            temp.append(temp2)
    matchedOutfits.extend(temp)
    return matchedOutfits


matches = pairOutfits()


print("Today's high is a nice " + str(round(maxTemp, 2)) + " degrees Farenheit.")
print("On the other hand, the low is " + str(round(minTemp,2)) + " degrees Farenheit.")
print("Additionally, the wind speed is " + str(windMPH) + " miles per hour.")
print("Based on this data, the clothes you tell me you own, and my own amazing fashion sense, I suggest wearing one of these outfits: ")
for m in matches:
    print(m)
