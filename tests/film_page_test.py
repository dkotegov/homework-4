# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import *
import unittest
from selenium import webdriver


# TODO: недавние страницы, футер

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()


class FilmPageTestCase(BaseTestCase):
    def test_awards_block(self):
        page = FilmPage(self.driver)

        # rate film logged
        page.open()
        page.film_block.login()
        result = page.film_block.rate_film()
        self.assertEqual(result, True)
        page.film_block.logout()

        # rate film not logged
        result = page.film_block.rate_film()
        self.assertEqual(result, False)

        page.open()
        # add film to watch list logged
        page.film_block.login()
        result = page.film_block.add_to_watch_list()
        self.assertEqual(result, True)
        page.film_block.add_to_watch_list() # second adding removes film from watch list
        page.film_block.logout()

        # add film to watch list not logged
        result = page.film_block.add_to_watch_list()
        self.assertEqual(result, False)

        # rate review logged
        page.open()
        page.film_block.login()
        result = page.film_block.like_review()
        self.assertEqual(result, True)
        page.refresh()
        result = page.film_block.dislike_review()
        self.assertEqual(result, True)
        page.film_block.logout()


