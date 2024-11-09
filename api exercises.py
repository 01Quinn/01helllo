import json

from Using_External_Interfaces import response

result = response
print(json.dumps)
for weather in result['weather']:
    print(weather["description"])

print("Temperature")
print(result["main"]["temp"])