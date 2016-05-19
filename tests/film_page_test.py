# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import *
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class FilmPageTestCase(BaseTestCase):
    def test_awards_block(self):
        page = FilmPage(self.driver)

        # rate film logged
        page.open()
        page.film_block.login()
        result = page.film_block.rate_film()
        self.assertTrue(result)
        page.film_block.logout()

        # rate film not logged
        result = page.film_block.rate_film()
        self.assertFalse(result)

        page.open()
        # add film to watch list logged
        page.film_block.login()
        result = page.film_block.add_to_watch_list()
        self.assertTrue(result)
        page.film_block.add_to_watch_list()  # second adding removes film from watch list
        page.film_block.logout()

        # add film to watch list not logged
        result = page.film_block.add_to_watch_list()
        self.assertFalse(result)

        # rate review logged
        page.open()
        page.film_block.login()
        result = page.film_block.like_review()
        self.assertTrue(result)
        page.refresh()
        result = page.film_block.dislike_review()
        self.assertTrue(result)
        page.film_block.logout()
