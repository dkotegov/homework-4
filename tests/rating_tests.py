import unittest
import os

from selenium.webdriver import DesiredCapabilities, Remote
import random
from selenium import webdriver
from Pages.auth_page import AuthPage
from Pages.film_page import FilmPage


class RatingTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_rate_new(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth_custom(auth_page.SIGNUP_LOGIN, "12345678")
        film_page = FilmPage(self.driver)
        film_page.PATH = "/film/2"
        film_page.open()
        choice = random.randint(1, 10)
        film_page.select_star(str(choice))
        film_page.submit_star()
        film_page.check_succes()

    def test_rate_success(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        film_page = FilmPage(self.driver)
        film_page.PATH = "/film/2"
        film_page.open()
        choice = random.randint(1, 10)
        film_page.select_star(str(choice))
        film_page.submit_star()
        film_page.check_succes()

    def test_rate_empty(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        film_page = FilmPage(self.driver)
        film_page.PATH = "/film/5"
        film_page.open()
        film_page.submit_star()
        check = film_page.check_not_succes()
        self.assertEqual(check, True)
