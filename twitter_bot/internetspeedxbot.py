import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

PROMISED_DOWN = 150
PROMISED_UP = 18
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
X_LOGIN_URL = "https://x.com/login"
SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        )
        self.chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        """
        Get the internet download and upload speed.
        """
        self.driver.get(SPEED_TEST_URL)
        # self.driver.implicitly_wait(2.5)
        go_button = self.driver.find_element(
            By.CSS_SELECTOR,
            "#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.start-button > a",
        )
        go_button.click()
        self.driver.implicitly_wait(120)
        download_speed_tag = self.driver.find_element(
            By.CSS_SELECTOR,
            "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span",
        )
        upload_speed_tag = self.driver.find_element(
            By.CSS_SELECTOR,
            "#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span",
        )
        self.download_speed = float(download_speed_tag.text)
        self.upload_speed = float(upload_speed_tag.text)
        print(
            f"Download Speed: {self.download_speed}\nUpload Speed: {self.upload_speed}"
        )
        self.driver.close()

    def tweet_at_provider(self):
        """
        Tweet at provider about bad internet service
        """
        if self.download_speed >= PROMISED_DOWN and self.upload_speed >= PROMISED_UP:
            print("You have promised internet speed")
        else:
            print("Nah fuck the telco!!😠")
            x_driver = webdriver.Chrome(options=self.chrome_options)
            x_driver.get(X_LOGIN_URL)
            x_driver.implicitly_wait(100)
            input_email = x_driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input',
            )
            input_email.send_keys(f"{TWITTER_EMAIL}")
            time.sleep(random.uniform(2, 4))
            next_btn = x_driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]',
            )
            next_btn.click()
