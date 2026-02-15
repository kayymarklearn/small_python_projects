import os
import requests

# API DATA
SHEETY_ENDPOINT = "https://api.sheety.co/cccd62b603ce6c457f24dc70f974bc88/flightDeals/prices"
BEARER_TOKEN = os.getenv("SHEETY_BEARER")

header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_flight_details(self) -> list[dict[str, str]]:
        """Returns a list of dictionaries containing {city, iataCode, lowestPrice}"""
        response = requests.get(url=SHEETY_ENDPOINT, headers=header)
        data = response.json()["prices"]
        
        return data
