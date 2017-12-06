from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config
from logger import log_d

from test.ok.LoginPage import LoginPage

class Case(TestCase):
    def setUp(self):
        self.browser = config.get("executor.browser.name", "CHROME")
        self.server_url = config["executor.scheme"] + "://" + config["executor.server"] + "/wd/hub"

        log_d("Try connect " + self.server_url)
        self.driver = Remote(
            command_executor=config["executor.scheme"] + "://" + config["executor.server"] + "/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, self.browser).copy()
        )

        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()

        self.loginModel = LoginPage(self.driver, config["login"], config["password"])

        self.loginModel.open()
        self.loginModel.auth()

        self.pages = []

    def tearDown(self):
        self.loginModel.close()

        for page in self.pages:
            page.close()

        self.driver.close()

    def addPage(self, page):
        self.pages.append(page)
