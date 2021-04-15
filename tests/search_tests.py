import unittest
import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from Pages.search_page import SearchPage


class SearchTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_search_film_success(self):
        string = "Корпорация монстров"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search(string)
        self.assertEqual(check, True)

    def test_search_film_unsuccess(self):
        string = "карпарация монстрав"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search(string)
        self.assertEqual(check, False)

    def test_search_user_success(self):
        string = "nnnnn"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search_user(string)
        self.assertEqual(check, True)

    def test_search_user_unsuccess(self):
        string = "nvjfdjvdnjfscjndsjcndjncjdns"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search_user(string)
        self.assertEqual(check, False)

    def test_search_person_success(self):
        string = "Александр"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search(string)
        self.assertEqual(check, True)

    def test_search_person_unsuccess(self):
        string = "осочльфч"
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.fill_search(string)
        check = search_page.check_search(string)
        self.assertEqual(check, False)
