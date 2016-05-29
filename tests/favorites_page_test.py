# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import FavoritesPage
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.page = FavoritesPage(self.driver)
        self.page.open()
        self.page.main_header.login()

    def tearDown(self):
        self.driver.quit()


class FavoritesPageTestCase(BaseTestCase):
    def test_click_film_title(self):
        self.page.fav_block.click_film_title()
        self.assertEqual(self.driver.current_url, self.page.fav_block.TEST_FILM_URL)

    def test_click_film_img(self):
        self.page.fav_block.click_film_img()
        self.assertEqual(self.driver.current_url, self.page.fav_block.TEST_FILM_URL)

    def test_click_film_city(self):
        self.page.fav_block.click_film_city()
        self.assertEqual(self.driver.current_url, self.page.fav_block.FILM_CITY_URL)

    def test_click_film_year(self):
        self.page.fav_block.click_film_year()
        self.assertEqual(self.driver.current_url, self.page.fav_block.FILM_YEAR_URL)

    def test_click_film_drama(self):
        self.page.fav_block.click_film_drama()
        self.assertEqual(self.driver.current_url, self.page.fav_block.DRAMA_BUTTON_URL)

    def test_click_film_comedy(self):
        self.page.fav_block.click_film_comedy()
        self.assertEqual(self.driver.current_url, self.page.fav_block.COMEDY_BUTTON_URL)

    def test_click_film_bio(self):
        self.page.fav_block.click_film_bio()
        self.assertEqual(self.driver.current_url, self.page.fav_block.BIO_BUTTON_URL)
