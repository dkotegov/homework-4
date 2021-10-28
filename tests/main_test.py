import unittest
from selenium import webdriver

from pages.main import MainPage
from pages.search import SearchPage


class MainTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testClickSearch(self):
        search = SearchPage(driver=self.driver)

        self.main.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickSearchWithParam(self):
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url, text=text), "Некорректный урл")

    def testEnterSearch(self):
        search = SearchPage(driver=self.driver)

        self.main.enter_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testEnterSearchWithParam(self):
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.enter_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url, text=text), "Некорректный урл")

    def tearDown(self):
        self.driver.close()
