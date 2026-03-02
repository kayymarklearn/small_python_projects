import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://ozh.github.io/cookieclicker/"

options = webdriver.ChromeOptions()  # pyright: ignore[reportCallIssue]
options.add_experimental_option("detach", True)
# options.add_argument("--headless")


driver = webdriver.Chrome(options=options)  # pyright: ignore[reportCallIssue]
driver.get(URL)


# Check if the language selection widget is present and select English
try:
    lang_select = WebDriverWait(driver, 2.5).until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    lang_select.click()
except:  # noqa: E722
    pass


driver.implicitly_wait(
    3
)  # Pause for all elements to finish loading (to prevent errors). I found out after tweaking that 3secs is the sweet spot.
start_time = time.monotonic()
start_5m = time.monotonic()
while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()
    now = time.monotonic()
    if now - start_time >= 5:
        # After every 5 seconds.
        cookies_money = driver.find_element(By.ID, "cookies")
        money = int(((cookies_money.text).split(" ")[0]).replace(",", ""))
        start_time = now

        # Get all product IDs
        item_ids = driver.find_elements(
            By.CSS_SELECTOR,
            "#products .product.unlocked.enabled",
        )

        # Create a list of all item prices to make comparison
        item_prices = []
        highest_price = 0
        for item in item_ids:
            item_prices.append(int((item.text.split()[1]).replace(",", "")))

        # Compare prices of all items to get the highest
        if len(item_prices) != 0:
            highest_price = max(item_prices)

        # Click on item to buy
        for item in item_ids:
            item_price = int(
                (item.text.split()[1]).replace(",", "")
            )  # Get the item's price
            # Check if the for the item with the highest price
            # check if there's enought money (cookies)
            if item_price >= highest_price and money >= item_price:
                # if there's enough money (cookies), click to buy
                item.click()
    if now - start_5m >= 300:
        # After every 5 minutes:
        cookies_per_second = driver.execute_script(
            'return document.getElementById("cookiesPerSecond").textContent'
        )

        # print the cookies per second to the terminal after every 5 mins
        print(f"Cookies/second: {cookies_per_second}")
        # start_5m = now # This will reset the timer to start counting to 5min
        break  # Or you can break the loop (essentially stopping the clicking after 5 mis)
        # If the break command is commented out or removed, the loop becomes perpetual.

driver.quit()  # Closes the browser
