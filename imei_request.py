import json
import requests


def imei_request(imei, token):
    url = 'https://api.imeicheck.net/v1/checks'
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
    }
    
    body =  json.dumps({
    "deviceId": imei
    })
    
    response = requests.post(url, headers=headers, data=body)
    return response.text
