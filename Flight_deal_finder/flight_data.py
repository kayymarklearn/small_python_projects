from data_manager import DataManager
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, current_location: str):
        self.flight = DataManager()
        self.flight_destinations = self.flight.get_flight_details()
        self.available_flights = []
        self.current_city = current_location
    

    def get_flights(self) -> dict[str, str]:
        """
        Docstring for get_flights
        
        :param self: Description
        Returns:
            a dictionary of city iata codes and their historical low prices
        """
        self.flight_search = FlightSearch(self.current_city)
        self.origin_iata = self.flight_search.get_origin_iata()
        for destination in self.flight_destinations:
            try:
                data = self.flight_search.search_flights(origin_iata=self.origin_iata, dest_iata=destination['iataCode'], max_price=destination["lowestPrice"]) # type: ignore
            except:
                pass
            else:
                if data != []:
                    price = data[0]["price"]["grandTotal"] # type: ignore
                    departure_port = data[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"] # type: ignore
                    departure_time = data[0]["itineraries"][0]["segments"][0]["departure"]["at"] # type: ignore
                    arrival_port = data[0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"] # type: ignore
                    arrival_time = data[0]["itineraries"][0]["segments"][0]["arrival"]["at"] # type: ignore
                    flight_data: dict[str, list[str]] = {
                        destination["city"]: [price, departure_port, departure_time, arrival_port, arrival_time]
                    }
                    self.available_flights.append(flight_data) # type: ignore


        return self.available_flights # type: ignore

        
