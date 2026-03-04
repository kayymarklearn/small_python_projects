import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIMILAR_ACCOUNT = "https://www.instagram.com/levrone_klever/"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

INSTA_LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(INSTA_LOGIN_URL)
        self.driver.implicitly_wait(10)
        # Enter username character by character to avoid detection
        input_user = self.driver.find_element(By.NAME, "email")
        for char in USERNAME:
            input_user.send_keys(char)
            time.sleep(0.05)
        time.sleep(random.uniform(2, 5))
        # Enter password character by character
        input_password = self.driver.find_element(By.NAME, "pass")
        for char in PASSWORD:
            input_password.send_keys(char)
            time.sleep(0.05)
        time.sleep(random.uniform(1.5, 4))
        input_password.send_keys(Keys.RETURN)

        time.sleep(5)
        # Handle "Save info" prompt if it appears
        try:
            save_info = self.driver.find_element(
                By.XPATH,
                '//button[contains(text(), "Save info")]',
            )
            save_info.click()
        except:
            pass

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers").click()

    def follow(self):
        time.sleep(5)
        # Find all follow buttons on the page
        followers = self.driver.find_elements(
            By.XPATH, '//button[.//div[text()="Follow"]]'
        )
        print(f"Found {len(followers)} follow buttons")

        # Follow each user with random delays
        for follower in followers:
            try:
                follower.click()
                time.sleep(random.uniform(3, 5))
            except Exception as e:
                print(f"Skipping: {e}")

        self.driver.get("https://www.instagram.com/")
