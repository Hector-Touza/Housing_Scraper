import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import numpy as np

from scraper.utils import hover


class IdealistaHouse:
    """
    A class to extract, store and save the features of a house in idealista.com
    #To do: should also save url

    """

    def __init__(self, driver):
        """
        Extract features from the web page and store them in a dict
        """
        self.driver = driver
        self.features = {}

        # ID in url
        self.features["ID"] = driver.current_url.split("/")[-2]

        # reference number in body
        self.features["reference"] = driver.find_element(By.CLASS_NAME, "txt-ref").text

        # Seller type
        self.features["seller_type"] = driver.find_element(By.CLASS_NAME, "name").text

        # Seller name
        self.features["seller_name"] = driver.find_element(By.NAME, "user-name").get_attribute("value")

        # zone
        self.features["zone"] = driver.find_element(By.CLASS_NAME, "main-info__title-minor").text

        # price
        self.features["asking_price"] = driver.find_element(By.CLASS_NAME, "info-data-price").text

        # tags
        self.features["tags"] = driver.find_element(By.CLASS_NAME, "info-features").text

        # features (array)
        self.features["features"] = driver.find_elements(By.CLASS_NAME, "details-property_features")[0].text.split("\n")

        # building (array)
        try:
            self.features["building"] = driver.find_elements(By.CLASS_NAME, "details-property_features")[1].text.split("\n")
        except:
            self.features["building"] = np.nan

        # appliances (array)
        try:
            self.features["appliances"] = driver.find_elements(By.CLASS_NAME, "details-property_features")[2].text.split("\n")
        except:
            self.features["appliances"] = np.nan

    def return_features(self):
        """
        Return extracted features as a dict
        """

        return self.features

    def next_house(self):
        """
        Navigates to the next house
        """

        self.driver.find_element(By.CSS_SELECTOR, "#pager > div > nav.detail-pagination--prev-next > a.btn.nav.next.icon-arrow-right-after").click()


class IdealistaCaptcha:
    """
    A class to solve the Idealista Captcha page
    """

    def __init__(self, driver):
        self.driver = driver

    def solve(self):
        """
        Hover over captcha and click it
        """

        # *************  locate CheckBox  **************
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#px-captcha > div > div > div > iframe"))
        )

        # *************  hover CheckBox  ***************
        rand = random.uniform(1.0, 1.5)
        print('\n\r explicit wait for ', rand, ' seconds before hovering')
        time.sleep(rand)
        hover(self.driver, checkbox)

        # *************  click CheckBox  ***************
        rand = random.uniform(0.5, 0.7)
        print('Explicit wait for ', rand, 'seconds before clicking')
        time.sleep(rand)
        # making click on CheckBox...
        click_return = checkbox.click()
        print(' Clicked on CheckBox with result: ', click_return, "\n\r")
