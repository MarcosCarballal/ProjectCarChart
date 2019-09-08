from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import pymysql


DEFAULT_HOST = '35.226.24.18'
DEFAULT_USER = 'root'
DEFAULT_PASS = 'pass'
DEFAULT_DB = 'cars'


# Parse GET contents into dict
def parse_get(request):

    keys = [
        "minYear",
        "maxYear",
        "minPrice",
        "maxPrice",
        "minSeats",
        "maxSeats",
        "minHorsePower",
        "maxHorsePower",
        "minEmissions",
        "maxEmissions"
    ]

    # Create dict and add the keys guaranteed to have vals
    search_dict = {
        "bodyType": request.GET.get("bodyType"),
        "fuelType": request.GET.get("fuelType")
        }


    for key in keys:
        val = ""
        val = request.GET.get(key)

        if (val is None or val == "" or not val.isdigit()):
            continue

        search_dict[key] = val

    return search_dict

    

def index(request):
    connection = pymysql.connect(host = DEFAULT_HOST, user = DEFAULT_USER,
            password = DEFAULT_PASS, db = DEFAULT_DB)
    sql = "SELECT * FROM cars.cars_info"
    cur = connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    context = {"results":results}
    return render_to_response('index_t.html',context)
# Create your views here.
