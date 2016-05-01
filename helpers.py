from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

BROWSER = os.environ['HW4BROWSER']

def tune_driver(page):
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, BROWSER).copy()
    )

    driver.get(page)
    driver.implicitly_wait(60)
    return driver