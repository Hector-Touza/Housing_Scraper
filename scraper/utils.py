import time
import subprocess
import platform
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import config.config as config


def start_webdriver():
    """
    Configure chrome webdriver & instance it.
    Supports Windows and Raspberry Pi
    :return: webdriver
    """

    # check if running on windows or Raspberry Pi & use appropriate command to start Chrome
    system = platform.system()
    if system == "Windows":
        subprocess.Popen('cmd /K start chrome.exe --profile-directory="Profile 1" --remote-debugging-port=5351 --disable-blink-features=AutomationControlled"')
    elif system == "Linux":
        subprocess.Popen(['lxterminal', '-e', 'google-chrome --profile-directory="Profile 1" --remote-debugging-port=5351 --disable-blink-features=AutomationControlled'])
    else:
        raise SystemError("Only Windows and Linux are supported")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:5351")  # Port numbers should match

    return webdriver.Chrome(options=options, executable_path=config.driver_path)


def hover(driver, element, delay=0.7):
    """
    Hover over given element
    """

    time.sleep(random.uniform(delay - 0.1, delay + 0.1))

    hov = ActionChains(driver).move_to_element(element)
    hov.perform()


if __name__ == "__main__":
    driver = start_webdriver()
    driver.get("https://www.idealista.com/venta-viviendas/barcelona/eixample/")
