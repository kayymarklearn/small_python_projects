import os
import time
from datetime import datetime
from twilio.rest import Client

# API DATA
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, current_city: str, flightlist):  # type: ignore
        self.message_template = """
Low price alert! Only £[price] to fly from [cur_loc]-[dep_port] to [dest]-[arrive_port],
from [dep_time] to [arrive_time]
"""
        self.current_city = current_city
        self.flights = flightlist
        self.notifications_list = []

    def get_messages(self):
        for flight in self.flights:
            for key, value in flight.items():
                destination = key
                price = flight[key][0]
                dep_port = flight[key][1]
                dep_time = datetime.strptime(
                    flight[key][2], "%Y-%m-%dT%H:%M:%S"
                ).strftime("%Y-%m-%d")
                arrive_port = flight[key][3]
                arrive_time = datetime.strptime(
                    flight[key][4], "%Y-%m-%dT%H:%M:%S"
                ).strftime("%Y-%m-%d")

                message = (
                    self.message_template.replace("[price]", price)
                    .replace("[cur_loc]", self.current_city)
                    .replace("[dep_port]", dep_port)
                    .replace("[dest]", destination)
                    .replace("[arrive_port]", arrive_port)
                    .replace("[dep_time]", dep_time)
                    .replace("[arrive_time]", arrive_time)
                )

                self.notifications_list.append(message)

    def send_notifications(self):
        self.get_messages()
        for notification in self.notifications_list:
            # send notifications with twilio
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_= twilio_number, body=notification, to=my_number
            )
            print(message.sid)
            if notification != self.notifications_list[-1]:
                time.sleep(60)
