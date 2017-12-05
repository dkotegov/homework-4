from selenium.webdriver.support.ui import WebDriverWait

from config import config

from logger import log_d

timeout = config["timeout"]

class Page(object):
    def __init__(self, driver, name_page="unknown"):
        self.url = config["ok.scheme"] + "://" + config["ok.server"]
        self.driver = driver

        self.name_page = name_page
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, path='/'):
        self.driver.get(self.url + path)

    def close(self):
        # some destruct, override me
        log_d("page " + self.name_page + " is destruct")