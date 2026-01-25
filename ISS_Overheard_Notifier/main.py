import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = "kayymark.learn@gmail.com"
MY_PASSWORD = os.getenv("MY_GMAIL_PASSWORD")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = { # type: ignore
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) # type: ignore
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# .................... Check if the ISS is close to my location ............................ #
if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <=5:
    if time_now >= sunset or time_now <= sunrise:
         with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=MY_EMAIL, 
                                msg=f"Subject:Look Up👆\n\nLook up, the ISS is above you in the sky."
                                )
    
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



