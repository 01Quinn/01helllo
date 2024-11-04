import requests
import json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
json_data = response.json()

print(json.dumps(json_data, indent=2))
print(json_data['value'])

