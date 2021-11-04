import requests
import json


class Processor:
    def __init__(self):
        self.response = requests.get(url="https://www.ing.nl/api/locator/atms/")
        self.data = self.parse_list(self.response.text)

    @staticmethod
    def parse_list(data):
        index = 0
        for i in range(0, len(str(data))):
            if data[i] == "[":
                index = i
                break

        return json.loads(data[index:])

