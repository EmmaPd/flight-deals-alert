import requests

ENDPOINT_SHEETY = "https://api.sheety.co/b4269237d0798949b901cd9a6e5de4f0/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_info(self):
        r = requests.get(url=ENDPOINT_SHEETY).json()
        self.destination_data = r["prices"]
        return self.destination_data

    def update_IATA(self):
        for city in self.destination_data:
            info = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            r = requests.put(url=F"{ENDPOINT_SHEETY}/{city['id']}", json=info)
            print(r.text)

