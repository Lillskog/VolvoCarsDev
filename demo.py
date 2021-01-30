import requests
import json
from config import * 

# API KEYS PLACED IN CONFIG.PY (VCC_API_KEY_PRIMARY, VCC_API_KEY_SECONDARY, DEMO_TOKEN)

url = 'https://api.volvocars.com/extended-vehicle/v1/vehicles'
resource_demo = url + '/YV4952NA4F120DEMO/resources'
odometer_demo = resource_demo + '/odometer'
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'authorization': 'Bearer ' + DEMO_TOKEN, 'vcc-api-key': VCC_API_KEY_PRIMARY}

r = requests.get(odometer_demo, headers=headers)

if r.status_code == 200:
    print(r.text)

if r.status_code == 400:
    raise Exception('Bad Request - Request contains an unaccepted input')
elif r.status_code == 401:
    raise Exception('Unauthorized')
elif r.status_code == 403:
    raise Exception('Resource forbidden')
elif r.status_code == 404:
    raise Exception('Not found')
elif r.status_code == 500:
    raise Exception('Internal Server Error')