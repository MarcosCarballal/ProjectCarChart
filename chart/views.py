from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import pymysql
import simplejson as json

DEFAULT_HOST = '35.226.24.18'
DEFAULT_USER = 'root'
DEFAULT_PASS = 'pass'
DEFAULT_DB = 'cars'
UNIX_SOCKET = '/cloudsql/pennapps-xx-252216:us-central1:pennapps-xx-instance'

    



def get_results_by_all_parameters(**kwargs):
    bodyType = None;fuelType = None; minYear = None; maxYear = None; minPrice = None; maxPrice = None; minSeats = None; maxSeats = None; minHorsePower = None; maxHorsePower = None; minEmissions = None; maxEmissions = None 

    for key,value in kwargs.items():
                    if key == "bodyType": bodyType  = value 
                    if key == "fuelType": fuelType  = value 
                    if key == "minYear": minYear  = value 
                    if key == "maxYear": maxYear  = value 
                    if key == "minPrice": minPrice  = value 
                    if key == "maxPrice": maxPrice  = value 
                    if key == "minSeats": minSeats  = value 
                    if key == "maxSeats": maxSeats  = value 
                    if key == "minHorsePower": minHorsePower  = value 
                    if key == "maxHorsePower": maxHorsePower  = value 
                    if key == "minEmissions": minEmissions  = value 
                    if key == "maxEmissions": maxEmissions  = value 

    #Determine how many predicates there are to begin with. Keeps track of predicates not yet put into select string
    predicate_count = 0
    if bodyType is not None : predicate_count+=1
    if fuelType is not None: predicate_count+=1
    if minYear is not None: predicate_count+=1
    if maxYear is not None: predicate_count +=1
    if minPrice is not None: predicate_count+=1
    if maxPrice is not None: predicate_count+=1
    if minSeats is not None: predicate_count+=1
    if maxSeats is not None: predicate_count+=1
    if minHorsePower is not None: predicate_count+=1
    if maxHorsePower is not None: predicate_count+=1
    if minEmissions is not None: predicate_count+=1
    if maxEmissions is not None: predicate_count+=1


    print("Predicate Count: " + str(predicate_count))
    sql = ""
    sql += "SELECT * from cars.cars_info WHERE "
### GET WHERE QUALIFIER
    num_params_left = predicate_count
    if(predicate_count==0):
        sql+= 'year >=2015'
    else:
        if bodyType is not None:
            sql += "bodyType="+ '"' +str(bodyType) + '"'
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if fuelType is not None:
            sql += "fuelType="+ '"' + str(fuelType) + '"'
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if minYear is not None:
            sql += "year >=" + minYear
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if maxYear is not None:
            sql += "year <="+maxYear
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if minPrice is not None:
            sql += "price >="+ minPrice
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if maxPrice is not None:
            sql += "price <="+ maxPrice
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if minSeats is not None:
            sql += "seats>="+ minSeats
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if maxSeats is not None:
            sql += "seats <="+ maxSeats
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if minHorsePower is not None:
            sql += "enginePower >="+ minHorsePower
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if maxHorsePower is not None:
            sql += "enginePower <="+maxHorsePower
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if minEmissions is not None:
            sql += "emissionsCO2 >="+minEmissions
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement
        if maxEmissions is not None:
            sql += "emissionsCO2 <="+maxEmissions
            if(num_params_left > 1):
                sql+= ' AND '
                num_params_left = num_params_left -1 #decrement

    print("SQL: " + sql)

    results = []

    try:
        #On the Google AppEngine
        connection = pymysql.connect(host = DEFAULT_HOST, user = DEFAULT_USER, password = DEFAULT_PASS, db = DEFAULT_DB,unix_socket = UNIX_SOCKET)
    except:
        # Ona local machine
        print("Connecting with unix socket failed... Attempting to connect as a local host... Look at views.py if you're confused")
        connection = pymysql.connect(host = DEFAULT_HOST, user = DEFAULT_USER,  password = DEFAULT_PASS, db = DEFAULT_DB)
    finally:
        cur = connection.cursor()
        cur.execute(sql)
        results = cur.fetchall()
    return results






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


def results_to_json(results):

    keys = [
        'bodyType', 
        'emissionsCO2', 
        'seatingCapacity', 
        'maxSpeed', 
        'fuelCapacity', 
        'fuelType', 
        'price', 
        'fuelConsumption', 
        'manufacturer', 
        'model', 
        'year', 
        'enginePower'
    ]

    json_list = []

    for result in results:
        new_dict = {}
        i = 0

        for key in keys:
            new_dict[key] = result[i]
            i += 1

        json_list.append(json.dumps(new_dict))

    return json_list
    

def index(request):
    connection = None;
    user_arguments = parse_get(request)
    results = get_results_by_all_parameters(**user_arguments)
    json_list = results_to_json(results)

    context = {"results":json_list}
    return render_to_response('index_t.html',context)
# Create your views here.
