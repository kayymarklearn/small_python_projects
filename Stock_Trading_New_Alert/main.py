import requests
from newsapi import (
    NewsApiClient, # type: ignore
)
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
VANTAGE_API_KEY = os.getenv("VANTAGE_API")
NEWS_API_KEY = os.getenv("NEWS_API")
NEWS_API_URL = "https://newsapi.org/v2/everything"
VANTAGE_API_PARAMETERS = {  # type: ignore
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": VANTAGE_API_KEY,
}

VANTAGE_API_URL = "https://www.alphavantage.co/query"

# TWILIO Details
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
MESSAGING_SERVICE_SID = os.getenv("MESSAGING_SERVICE_SID")
MY_NUMBER = os.getenv("MY_NUMBER")

news = []
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
vantage_response = requests.get(VANTAGE_API_URL, params=VANTAGE_API_PARAMETERS)  # type: ignore
vantage_response.raise_for_status()
vantage_response_data = vantage_response.json()["Time Series (Daily)"]
yesterday_close = list(vantage_response_data.values())[:1][0]["4. close"]
day_before_close = list(vantage_response_data.values())[1:2][0]["4. close"]
price_change = float(yesterday_close) - float(day_before_close)
percentage_change = ((price_change) / float(yesterday_close)) * 100
if percentage_change < 0:
    percentage_change_str = f"🔻{abs(round(percentage_change))}%"
else:
    percentage_change_str = f"🔺{abs(round(percentage_change))}%"

if (abs(percentage_change)) >= 5:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_data = NewsApiClient(api_key=NEWS_API_KEY)  # type: ignore
    news_response = news_data.get_everything(q=COMPANY_NAME)  # type: ignore

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    for article in news_response["articles"][:3]:  # type: ignore
        message: str = (
            f"{COMPANY_NAME} {percentage_change_str}\nHeadline: {article["title"]}\nBrief: {article["description"]}"
        )
        news.append(message)  # type: ignore

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in news: # type: ignore
        message = client.messages.create(
            messaging_service_sid=MESSAGING_SERVICE_SID, body=article, to=MY_NUMBER # type: ignore
        )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
