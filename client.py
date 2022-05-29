from http import client
from iiot_device import Sensor
import json
import time

#Creacion de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost',port=5000)

#Creacion de un objeto de la clase Sensor
s=Sensor()

#pa formar el json que se va pal servidor
headers1={'Content-type':'application/json'}


while True:
    data= {
        'id':1,
        'name':'Base',
        'value': s.get_random_number()
    }

    json_data= json.dumps(data)

    _conn.request('POST','/devices',json_data,headers=headers1)
    _conn.close()


    #Makes the comparison to decide if there needs to be a warning or not
    base = data['value']
    if base > 15:
        print("Warning: The base is not stable=",base,"°")
    else:
        print("The base is stable",base,"°")
    
    
    #print(s.get_random_number())
    #print(s.get_temp_for_windows())
    time.sleep(1)
