from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import pymysql

DEFAULT_HOST = '35.226.24.18'
DEFAULT_USER = 'root'
DEFAULT_PASS = 'pass'
DEFAULT_DB = 'cars'
UNIX_SOCKET = '/cloudsql/pennapps-xx-252216:us-central1:pennapps-xx-instance'


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
