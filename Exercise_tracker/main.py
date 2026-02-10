import requests
import json
from datetime import datetime
import os

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER = os.getenv("SHEETY_BEARER")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER}"
}

headers = {
    "x-goog-api-key": GEMINI_API_KEY,
    "Content-Type": "application/json"
}

data = {
    "contents": [{
        "parts": [{
            "text": f"Parse this exercise log: '{input("Tell me which exercise you did: ")}'. Extract exercises, estimate calories burned (assume average adult), and duration."
        }]
    }],
    "generationConfig": {
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "object",
            "properties": {
                "exercises": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string"},
                            "duration": {"type": "string"},
                            "calories_burned": {"type": "integer"}
                        },
                        "required": ["type", "calories_burned", "duration"]
                    }
                }
            }
        }
    }
}

response = requests.post(endpoint, json=data, headers=headers)
exercises = json.loads(response.json()['candidates'][0]['content']['parts'][0]['text'])['exercises']



# with open("data.json", "w") as file:
#     json.dump(exercises, file, indent=4)

# Getting current date and time
today = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")



for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": f"{today}",
            "time": f"{current_time}",
            "exercise": f"{exercise['type'].title()}",
            "duration": f"{exercise['duration'].split()[0]}",
            "calories": f"{exercise['calories_burned']}"
        }
    }

    print(f"\nSending to Sheety: {json.dumps(sheety_data, indent=2)}")

    response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
