from env_conf import get_browser_name, CHROME_NAME, FIREFOX_NAME

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def get_webdriver():
    browser_name = get_browser_name()
    if browser_name == CHROME_NAME:
        return webdriver.Chrome()
    if browser_name == FIREFOX_NAME:
        return webdriver.Firefox()