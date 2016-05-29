# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import RatingsPage
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.page = RatingsPage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()


class RatingsPageTestCase(BaseTestCase):
    def test_click_import_rating(self):
        self.page.ratings_block.click_import_rating()
        self.assertEqual(self.driver.current_url, self.page.ratings_block.IMPORT_RATING_URL)

    def test_click_choose_film(self):
        self.page.ratings_block.click_choose_film()
        self.assertEqual(self.driver.current_url, self.page.ratings_block.CHOOSE_FILM_URL)

    def test_click_choose_series(self):
        self.page.ratings_block.click_choose_series()
        self.assertEqual(self.driver.current_url, self.page.ratings_block.CHOOSE_SERIES_URL)

    def test_click_choose_tvshow(self):
        self.page.ratings_block.click_choose_tvshow()
        self.assertEqual(self.driver.current_url, self.page.ratings_block.CHOOSE_TVSHOW_URL)
