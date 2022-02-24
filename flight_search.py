import requests
from datetime import datetime, timedelta
from pprint import pprint
from flight_data import FlightData

API_KEY_KIWI = "xbOgQZp2RGLOpmfmDGXTA6215I5wFkeH"
ENDPOINT_KIWI = "https://tequila-api.kiwi.com"

tomorrow = datetime.now() + timedelta(days=1)
six_mo = datetime.now() + timedelta(days=180)

START_DATE = tomorrow.strftime("%d/%m/%Y")
END_DATE = six_mo.strftime("%d/%m/%Y")

ORIGIN_CITY_IATA = "BUH"

class FlightSearch:

    def get_destination_code(self, location):
        header = {"apikey": API_KEY_KIWI}
        query = {
            "term": location,
            "location_types": "city"
        }
        r = requests.get(url=f"{ENDPOINT_KIWI}/locations/query", headers=header, params=query).json()
        code = r["locations"][0]["code"]
        return code

    def check_flights(self, iata_code):
        header = {"apikey": API_KEY_KIWI}
        destination_info = {
            "fly_from": ORIGIN_CITY_IATA,
            "fly_to": iata_code,
            "date_from": START_DATE,
            "date_to": END_DATE,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 5,
            "flight_type": "round",
            "max_stopovers": 0,
            "one_for_city": 1
        }

        r = requests.get(url=F"{ENDPOINT_KIWI}/v2/search", params=destination_info, headers=header).json()
        # pprint(r)

        try:
            r["data"][0]
        except IndexError:
            print(f"No flights found for {iata_code}.")
            return None

        flight_data = FlightData(
            price=r["data"][0]["conversion"]["EUR"],
            origin_city=r["data"][0]["cityFrom"],
            origin_airport=r["data"][0]["flyFrom"],
            destination_city=r["data"][0]["cityTo"],
            destination_airport=r["data"][0]["flyTo"],
            out_date=r["data"][0]["local_departure"].split("T")[0],
            return_date=r["data"][0]["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {flight_data.price} EUR")
        return flight_data
