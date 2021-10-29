import requests
import json

CONF = Cfg(os.environ.get(constants.STAGE))

response = requests.get(url="https://www.ing.nl/api/locator/atms/")

output = str(response.text)

for i in range(0, len(output)):
    if output[i] == "[":
        index = i
        break

real_string = output[6:]

new_output = json.loads(real_string)[0]

print(new_output)
