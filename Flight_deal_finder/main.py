from flight_data import FlightData
from notification_manager import NotificationManager

current_location = input("What is your current city: ").upper()

flightdata: FlightData = FlightData(current_location)
flights = flightdata.get_flights() # type: ignore

notification: NotificationManager = NotificationManager(current_city=current_location, flightlist=flights)
notification.send_notifications()

