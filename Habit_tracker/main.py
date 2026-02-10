import requests
import os
from datetime import datetime


# Constants and variables
USERNAME = os.getenv("USERNAME")
USER_TOKEN = os.getenv("USER_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_id = "graph01"
PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{graph_id}"

# Create user in pixela using the API

    # Data for creating user post request
# user_body = {
#     "token": f"{USER_TOKEN}",
#     "username": f"{USERNAME}",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# # Create post request to create user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_body)
# print(response.status_code)
# print(response.text)

# Create a graph for our user using the API
# graph_header = {
#     "X-USER-TOKEN": USER_TOKEN
# }

#     # Data for the graph request body
# graph_body = {
#     "id": graph_id,
#     "name": "Reading Tracker",
#     "unit": "pages",
#     "type": "int",
#     "color": "ajisai",
#     "startOnMonday": True
# }

# Create post request to create graph

# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_body, headers=graph_header)
# print(response.status_code)
# print(response.text)

# Create or Add a pixel using API (post request)

date = datetime.now().strftime("%Y%m%d")
# while True:
#     try:
#         number_of_pages_read = input("Write the number of pages you read: ")
#         int(number_of_pages_read) # Validate that input is an integer, don't store
#         break
#     except ValueError:
#         print("That's not a number! Please enter a number.")


pixel_header = {
    "X-USER-TOKEN": USER_TOKEN
}

# pixel_body = {
#     "date": date,
#     "quantity": number_of_pages_read
# }

# Make post request to add pixel for the day
# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_body, headers=pixel_header)
# print(response.status_code)
# print(response.text)

# Update pixel for a date
UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/{date}"
# update_pixel_body = {
#     "quantity": number_of_pages_read
# }

# Updating pixel using Put request
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_body, headers=pixel_header)
# print(response.status_code)
# print(response.text)

# Deleting a particular pixel using Delete request
DELETE_PIXEL_ENDPOINT = UPDATE_PIXEL_ENDPOINT
response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=pixel_header)
print(response.status_code)
print(response.text)