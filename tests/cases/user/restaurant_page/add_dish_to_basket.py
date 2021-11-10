import os

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver import DesiredCapabilities, Remote
# from selenium.webdriver.support.ui import WebDriverWait


class AddDishToBasketTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://delivery-borscht.ru')
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='https://delivery-borscht.ru',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.assertTrue(1 == 1, '1 == 1')
