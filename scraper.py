import requests
import json
import re
from ttictoc import TicToc
from bs4 import BeautifulSoup

baseurl = 'https://www.cars-data.com/en/abarth-124-spider-1.4-multiair-16v-specs'

cars = []

def parseIndividualCarInfo(carID):
    rawData = getRawResponse(carID)
    soup = getSoup(rawData)
    jsonData = getIndividualCarJSONData(soup)
    price = getPrice(soup)
    return jsonData, price

def getRawResponse(carID):
    url = "{}/{}/tech".format(baseurl, carID)
    return requests.get(url)

def getSoup(rawResponse):
    return BeautifulSoup(rawResponse.text, "html.parser")

def getIndividualCarJSONData(soup):
    result = soup.find("script", {"type": "application/ld+json"})
    data = result.contents[0]
    return json.loads(data.string)

def getPrice(soup):
    result = soup.find("dt", string="price:").next_sibling.contents[0].split()[1].replace('.', '')  #ugly i know
    return result

def getCarJSON(carID):
        jsonData, price = parseIndividualCarInfo(carID)

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
            fuelConsumption = fuelConsumption.split()[0].replace(',', '.')

        emissionsCO2 = jsonData['emissionsCO2'] if jsonData['emissionsCO2'] else None
        if emissionsCO2:
            emissionsCO2 = emissionsCO2.split()[0]

        car = {"bodyType": jsonData['bodyType'] if jsonData['bodyType'] else None,
                "emissionsCO2": emissionsCO2,
                "seatingCapacity": jsonData['seatingCapacity'] if jsonData['seatingCapacity'] else None,
                "maxSpeed": maxSpeed,
                "fuelCapacity": fuelCapacity,
                "fuelType": jsonData['fuelType'] if jsonData['fuelType'] else None,
                "price": price,
                "fuelConsumption": fuelConsumption,
                "manufacturer": jsonData['manufacturer']['name'] if jsonData['manufacturer']['name'] else None,
                "model": jsonData['model'] if jsonData['model'] else None,
                "year": jsonData['vehicleModelDate'] if jsonData['vehicleModelDate'] else None,
                "enginePower": enginePower
                }

        return car

def findAllBrands():
    url = 'https://www.cars-data.com/en/car-brands-cars-logos.html'
    rawResponse = requests.get(url)
    soup = getSoup(rawResponse)
    results = soup.findAll("option", {"value" : re.compile(r".+")})

    baseurl = 'https://www.cars-data.com/en/'
    for result in results[:1]:          #get rid of [:...] to check all     #each brand/make
        make = result.attrs['value']
        url = "{}{}".format(baseurl, make)
        findAllModels(url)

def findAllModels(url):
    rawResponse = requests.get(url)
    soup = getSoup(rawResponse)
    results = soup.findAll("a", {"href" : re.compile(r"{0}/.*".format(url))})

    for result in results[2:]:      #each model
        url = result.attrs['href']
        findAllYears(url)

def findAllYears(url):
    rawResponse = requests.get(url)
    soup = getSoup(rawResponse)
    urlPart1 = url.rsplit('/',1)[0]
    urlPart2 = url.rsplit('/',1)[-1]
    results = soup.findAll("a", {"href" : re.compile(r"{0}-{1}.*".format(urlPart1, urlPart2))})

    for result in results:      #each year
        url = result.attrs['href']
        findAllVariations(url)

def findAllVariations(url):
    rawResponse = requests.get(url)
    soup = getSoup(rawResponse)
    results = soup.findAll("a", {"href" : re.compile(r"specs/.*")})

    for result in results:      #each variation
        url = result.attrs['href']
        carID = url.rsplit('/',1)[-1]
        print(getCarJSON(carID))


# findAllBrands()
# findAllModels('https://www.cars-data.com/en/abarth')
# findAllYears('https://www.cars-data.com/en/ford/focus')
# findAllVariations('https://www.cars-data.com/en/ford-focus-1998/753')

# for i in range(1, 80000, 10000):
#     print(getCarJSON(i))
