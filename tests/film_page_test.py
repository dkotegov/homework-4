# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import FilmPage
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.page = FilmPage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()


class FilmPageTestCase(BaseTestCase):
    def test_rate_film_not_logged(self):
        result = self.page.film_block.rate_film()
        self.assertFalse(result)

    def test_add_film_not_logged(self):
        result = self.page.film_block.add_to_watch_list()
        self.assertFalse(result)

    def test_add_film_logged(self):
        self.page.film_block.login()
        result = self.page.film_block.add_to_watch_list()
        self.assertTrue(result)
        self.page.film_block.add_to_watch_list()
        self.page.film_block.logout()

    def test_rate_film_logged(self):
        self.page.film_block.login()
        result = self.page.film_block.rate_film()
        self.assertTrue(result)
        self.page.film_block.logout()


    def test_like_review(self):
        self.page.film_block.login()
        result = self.page.film_block.like_review()
        self.assertTrue(result)
        self.page.refresh()
        result = self.page.film_block.dislike_review()
        self.assertTrue(result)
        self.page.film_block.logout()
