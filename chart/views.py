from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import pymysql

DEFAULT_HOST = '35.226.24.18'
DEFAULT_USER = 'root'
DEFAULT_PASS = 'pass'
DEFAULT_DB = 'cars'
UNIX_SOCKET = '/cloudsql/pennapps-xx-252216:us-central1:pennapps-xx-instance'

    
def get_results_by_all_parameters(self,**kwargs):
            bodyType = None;fuelType = None; minYear = None; maxYear = None; minPrice = None; maxPrice = None; minPrice = None; maxPrice = None; minSeats = None; maxSeats = None; minHorsePower = None; maxHorsePower = None; minEmissions = None; maxEmissions = None 

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
            if name is not None: predicate_count+=1
            if boot_mode is not None: predicate_count+=1
            if build is not None: predicate_count+=1
            if pon_mode is not None: predicate_count+=1
            if device is not None: predicate_count+=1
            if release is not None: predicate_count+=1
            total_parameters = predicate_count

            print("Predicate Count: " + str(predicate_count))

            select = "SELECT * FROM " + self.test_results_table_name + " WHERE"
            select += self.get_where_qualifier_by_all_parameters(total_parameters,status,requirement,name ,boot_mode , build ,pon_mode,device ,release)
            if(total_parameters == 0):
                    select = select.split('WHERE')[0]
            results = self._db_fetch_rows(select)
    
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

    

def index(request):
    connection = None;
    try:
        #On the Google AppEngine
        connection = pymysql.connect(host = DEFAULT_HOST, user = DEFAULT_USER, password = DEFAULT_PASS, db = DEFAULT_DB,unix_socket = UNIX_SOCKET)
    except:
        # Ona local machine
        print("Connecting with unix socket failed... Attempting to connect as a local host... Look at views.py if you're confused")
        connection = pymysql.connect(host = DEFAULT_HOST, user = DEFAULT_USER,  password = DEFAULT_PASS, db = DEFAULT_DB)
    finally:

        sql = "SELECT * FROM cars.cars_info"
        cur = connection.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        json_list = []

        context = {"results":results}
        return render_to_response('index_t.html',context)
# Create your views here.
