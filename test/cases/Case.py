from unittest import TestCase

from selenium import webdriver

from config import config
from logger import log_d

from test.ok.LoginPage import LoginPage

class Case(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
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
