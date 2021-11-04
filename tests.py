import requests
import json

response = requests.get(url="https://www.ing.nl/api/locator/atms/")

output = str(response.text)

for i in range(0, len(output)):
    if output[i] == "[":
        index = i
        break

new_output = json.loads(output[index:])

print(new_output[0])





