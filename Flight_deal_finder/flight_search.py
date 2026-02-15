import os
import json
import requests
from datetime import datetime, timedelta

# API DATA
API_KEY = os.getenv("AMD_KEY")
API_SECRET = os.getenv("AMD_SECRET")
AMA_ENDPOINT = "https://test.api.amadeus.com/v2"

# ACCESS_TOKEN = "2RhfpM2JmhEodJ6OFONFtB9s4007"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, current_location: str):
        self.access_token = self.get_access_token()
        self.access_header = {"Authorization": f"Bearer {self.access_token}"}
        self.current_city = current_location
    
    def get_access_token(self) -> str:
        """Get an access token to query amadeus API"""
        AMA_ACCESS_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
            # "Authorization": f"Bearer {self.access_token}"
        }

        parameters = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        response = requests.post(url=AMA_ACCESS_ENDPOINT, data=parameters, headers=header)
        token = json.loads(response.text)["access_token"]
        return token
    def get_origin_iata(self) -> str:
        """
        Docstring for get_origin_iata
        
        :param self: Description
        :return: iata code of the current location of the costumer
        :rtype: str
        """
        # current_city = input("What is your current city: ").upper()
        search_iata_endpoint = f"https://test.api.amadeus.com/v1/reference-data/locations/cities"
        origin_params = { # type: ignore
            "keyword": self.current_city,
            "max": 1
        }
        response = requests.get(url=search_iata_endpoint, params=origin_params, headers=self.access_header) # type: ignore
        city_iata = response.json()['data'][0]["iataCode"]

        return city_iata


    def search_flights(self, origin_iata: str, dest_iata: str, max_price=None): # type: ignore
        """
        Search for
        
        :param self: Description
        :param origin_iata: iata code of the current location
        :type origin_iata: str
        :param dest_iata: iata code of the destination 
        :type dest_iata: str
        :param max_price: max_price you're willing to pay
        :type max_price: None

        Returns:
            dict: Flight data search results from API
        """
        AMA_FLIGHT_SEARCH_ENDPOINT = f"{AMA_ENDPOINT}/shopping/flight-offers"
        self.access_header = {"Authorization": f"Bearer {self.access_token}"}
        all_flights = []

        for days_ahead in range(0, 180, 7):
            departure_time = (datetime.now() + timedelta(days=days_ahead)).strftime("%Y-%m-%d")

            search_params = { # type: ignore
                "originLocationCode": origin_iata,
                "destinationLocationCode": dest_iata,
                "departureDate": departure_time,
                "adults": 1,
                "max": 1
            }
            if max_price:
                search_params["maxPrice"] = max_price
            
            response = requests.get(url=AMA_FLIGHT_SEARCH_ENDPOINT, headers=self.access_header, params=search_params) # type: ignore

            if response.json().get("data"):
                all_flights.extend(response.json()["data"]) # type: ignore

        # Find the cheapest flights
        if all_flights:
            min_price = min(float(flight['price']['grandTotal']) for flight in all_flights) # type: ignore
            cheapest_flights = [flight for flight in all_flights if float(flight['price']['grandTotal']) == min_price] # type: ignore
            return cheapest_flights # type: ignore
        else:
            return [] # type: ignore




