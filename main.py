from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

notification_manager = NotificationManager()
sheet = DataManager()
sheet_data = sheet.get_info()
flight_search = FlightSearch()

# for city in sheet_data:
#     if city["iataCode"] == "":
#         city["iataCode"] = flight_search.get_destination_code(city["city"])
#         sheet.update_IATA()
#
#
# for city in sheet_data:
#     iata_code = city["iataCode"]
#     flight = flight_search.check_flights(iata_code)
#     try:
#         if flight.price < city["lowestPrice"]:
#             notification_manager.send_sms(message=f"Low alert price! 🧨\nOnly {flight.price} EUR to fly "
#                                                     f"from {flight.origin_city}-{flight.origin_airport} to "
#                                                     f"{flight.destination_city}-{flight.destination_airport}, from "
#                                                     f"{flight.out_date} to {flight.return_date}")
#     except AttributeError:
#         pass
#

print(sheet.destination_data)