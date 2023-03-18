import requests
import json

print("***Light Price Checker***")

#config params
url = 'https://api.esios.ree.es/indicators/102'
headers = {'Accept': 'application/json'}
params = {'start_date': '2023-03-17T00:00:00Z', 'end_date': '2023-03-17T23:59:59Z'}

#respons and data
response = requests.get(url, headers=headers, params=params)
data = json.loads(response.text)

values = data['indicator']['values']
for value in values:
    timestamp = value['datetime']
    price = value['value']
    print(f'En el momento {timestamp} el precio fue de {price} €/MWh')