import requests
import json
from ttictoc import TicToc
from bs4 import BeautifulSoup

baseurl = 'https://www.cars-data.com/en/abarth-124-spider-1.4-multiair-16v-specs'

cars = []

def getAllCarInfo(carID):
    rawData = getRawResponse(carID)
    soup = getSoup(rawData)
    jsonData = getJSONData(soup)
    return jsonData

def getRawResponse(carID):
    url = "{}/{}/tech".format(baseurl, carID)
    return requests.get(url)

def getSoup(rawResponse):
    return BeautifulSoup(rawResponse.text, "html.parser")

def getJSONData(soup):
    result = soup.find("script", {"type": "application/ld+json"})
    data = result.contents[0]
    return json.loads(data.string)

def scrape():
    for i in range(1, 2):
        jsonData = getAllCarInfo(carID=i)

        engineInfo = jsonData['vehicleEngine'] if jsonData['vehicleEngine'] else None
        enginePower = None
        if engineInfo:
            enginePower = engineInfo['enginePower'] if engineInfo['enginePower'] else None
            if enginePower:
                enginePower = enginePower.split()[0]

        maxSpeed = jsonData['speed'] if jsonData['speed'] else None
        if maxSpeed:
            maxSpeed = maxSpeed.split()[0]

        fuelCapacity = jsonData['fuelCapacity'] if jsonData['fuelCapacity'] else None
        if fuelCapacity:
            fuelCapacity = fuelCapacity.split()[0]

        fuelConsumption = jsonData['fuelConsumption'] if jsonData['fuelConsumption'] else None
        if fuelConsumption:
            fuelConsumption = fuelConsumption.split()[0]

        emissionsCO2 = jsonData['emissionsCO2'] if jsonData['emissionsCO2'] else None
        if emissionsCO2:
            emissionsCO2 = emissionsCO2.split()[0]

        car = {"bodyType": jsonData['bodyType'] if jsonData['bodyType'] else None,
                "emissionsCO2": emissionsCO2,
                "seatingCapacity": jsonData['seatingCapacity'] if jsonData['seatingCapacity'] else None,
                "maxSpeed": maxSpeed,
                "fuelCapacity": fuelCapacity,
                "fuelType": jsonData['fuelType'] if jsonData['fuelType'] else None,
                "price": "46760",
                "fuelConsumption": fuelConsumption,
                "manufacturer": jsonData['manufacturer']['name'] if jsonData['manufacturer']['name'] else None,
                "model": jsonData['model'] if jsonData['model'] else None,
                "year": jsonData['vehicleModelDate'] if jsonData['vehicleModelDate'] else None,
                "enginePower": enginePower,
                "energyRating": "F"
                }

scrape()