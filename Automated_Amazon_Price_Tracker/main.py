from dotenv import load_dotenv
from bs4 import BeautifulSoup
from smtplib import SMTP
import requests
import os

load_dotenv()
URL = "https://appbrewery.github.io/instant_pot/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Accept-Language": "en-US,en;q=0.9"
}
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# A target price for when our product is below this price, in this case $100
price_target = float(100)
response = requests.get(URL, headers=headers)

site = BeautifulSoup(response.text, "html.parser")
price_tag = site.select_one(selector="div span .a-price-whole")
price_decimal_tag = site.select_one(selector="div span .a-price-fraction")
price_decimal = price_decimal_tag.getText()
price = price_tag.getText()
whole_price = float(price + price_decimal)
product_title = (site.select_one(selector="#productTitle")).getText()

product_title = " ".join(product_title.split())


subject = "Amazon Price Alert!"
body = f"{product_title} is now ${whole_price}"
message = f"Subject: {subject}\n\n{body}".encode('utf-8')

if whole_price < price_target:
    with SMTP(host=SMTP_ADDRESS, port=587) as  server:

        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
