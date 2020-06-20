import json

from scraper.utils import start_webdriver
from scraper.pages import *

import config.config as config

# Start webdriver and delete cookies
driver = start_webdriver()
driver.delete_all_cookies()

# Navigate to specified area page
driver.get(config.starting_url)
time.sleep(random.uniform(3, 3.2))

# find first house and access it
driver.find_element(By.CLASS_NAME, "item-info-container").click()

data = []
counter = 1

while True:
    time.sleep(random.uniform(1.2, 1.4))

    # check if we loaded house or captcha
    try:
        house = IdealistaHouse(driver)
    except:
        captcha = IdealistaCaptcha(driver)
        captcha.solve()

        time.sleep(random.uniform(5.2, 5.4))
        house = IdealistaHouse(driver)

    # get features
    feats = house.return_features()
    data.append(feats)

    print(f'''Scrapped House {feats.get("ID")}. Total: {counter}''')
    counter += 1

    # navigate to next. if no more houses break
    try:
        house.next_house()
    except:
        break


with open("data_barcelona_eixample_parcial_16_05_20.json", 'w') as f:
    # indent=2 to make the file more human-readable
    json.dump(data, f, indent=2)
