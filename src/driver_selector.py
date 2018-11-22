from env_conf import get_browser_name, CHROME_NAME, FIREFOX_NAME

from selenium import webdriver


def get_webdriver():
    browser_name = get_browser_name()
    if browser_name == CHROME_NAME:
        return webdriver.Chrome()
    if browser_name == FIREFOX_NAME:
        return webdriver.Firefox()