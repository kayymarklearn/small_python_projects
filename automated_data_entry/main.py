import random
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdPBbq6yoQyxWdtrgNqcgodzUXoheMl-rxLCtJJij6SW9Z12Q/viewform?usp=publish-editor"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
zillow = BeautifulSoup(response.text, "html.parser")

# Get a list of all the prices [in order] since python lists preserve insertion order
price_lines = zillow.find_all("span", {"data-test": "property-card-price"})
prices = [price.get_text().split("+")[0].split("/")[0] for price in price_lines]

# Get a list of all address [in order] since python lists preserve insertion order
address_lines = zillow.find_all("address", {"data-test": "property-card-addr"})
addresses = [
    address.get_text().strip("\n").strip(" ").strip("\n") for address in address_lines
]

property_links = zillow.find_all("a", {"class": "StyledPropertyCardDataArea-anchor"})
links = [link.get("href") for link in property_links]

# setup chrome chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
form = webdriver.Chrome(options=options)
wait = WebDriverWait(form, 10)
form.get(FORM_URL)


for i in range(len(prices)):
    form_inputs = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd")))

    form_inputs = form.find_elements(By.CLASS_NAME, "whsOnd")
    address_input = form_inputs[0]
    price_input = form_inputs[1]
    link_input = form_inputs[2]

    for char in addresses[i]:
        address_input.send_keys(char)
        time.sleep(random.uniform(0.05, 0.1))

    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    # submit a response
    submit_button = form.find_element(By.CSS_SELECTOR, "[aria-label='Submit']")
    submit_button.click()

    # Submit next response
    time.sleep(random.uniform(1, 4))
    submit_another = form.find_element(By.LINK_TEXT, "Submit another response")
    submit_another.click()

print("All done, Rent details have been submitted to google form!!")
form.quit()
