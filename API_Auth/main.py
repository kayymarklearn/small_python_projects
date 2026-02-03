import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("API_KEY")
URL="https://api.openweathermap.org/data/2.5/forecast"
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


parameters: dict[str, str | int] = {
    'lat': "7.872014",
    'lon': "-5.475334",
    'appid': API_KEY,
    "cnt": 4
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    if int(item["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
    .create(
        body ="It's going to rain today. Remember to bring an ☂️",
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)
