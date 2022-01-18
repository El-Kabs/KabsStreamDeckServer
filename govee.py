import requests
import json
import os

def prenderLuces(data):
    headers = {'Govee-API-Key': os.environ.get('goveeapikey')}

    r = requests.get('https://developer-api.govee.com/v1/devices', headers=headers)
    data = json.loads(r.text)

    device = data['data']['devices'][0]['device']
    model = data['data']['devices'][0]['model']

    dataSend = {
        'device': device,
        'model': model,
        'cmd': {"name": "turn", "value": "on"}
    }

    r = requests.put('https://developer-api.govee.com/v1/devices/control', headers=headers, json=dataSend)

def apagarLuces(data):
    headers = {'Govee-API-Key': os.environ.get('goveeapikey')}

    r = requests.get('https://developer-api.govee.com/v1/devices', headers=headers)
    data = json.loads(r.text)

    device = data['data']['devices'][0]['device']
    model = data['data']['devices'][0]['model']

    dataSend = {
        'device': device,
        'model': model,
        'cmd': {"name": "turn", "value": "off"}
    }

    r = requests.put('https://developer-api.govee.com/v1/devices/control', headers=headers, json=dataSend)

def cambiarColor(dataP):
    red = dataP['r']
    g = dataP['g']
    b = dataP['b']
    headers = {'Govee-API-Key': os.environ.get('goveeapikey')}

    r = requests.get('https://developer-api.govee.com/v1/devices', headers=headers)
    data = json.loads(r.text)

    device = data['data']['devices'][0]['device']
    model = data['data']['devices'][0]['model']

    dataSend = {
        'device': device,
        'model': model,
        'cmd': {"name": "color", "value": {"r": red, "g": g, "b": b}}
    }

    r = requests.put('https://developer-api.govee.com/v1/devices/control', headers=headers, json=dataSend)
    print(r.text)

def cambiarBrillo(dataP):
    brillo = int(dataP['brillo'])
    headers = {'Govee-API-Key': os.environ.get('goveeapikey')}

    r = requests.get('https://developer-api.govee.com/v1/devices', headers=headers)
    data = json.loads(r.text)

    device = data['data']['devices'][0]['device']
    model = data['data']['devices'][0]['model']

    dataSend = {
        'device': device,
        'model': model,
        'cmd': {"name": "brightness", "value": brillo}
    }

    r = requests.put('https://developer-api.govee.com/v1/devices/control', headers=headers, json=dataSend)
