import unittest

from selenium import webdriver


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()
