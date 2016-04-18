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


class FavoritesPageTestCase(BaseTestCase):

    """
    def test_films_button(self):
        page.fav_block.click_films_button()
        self.assertEqual(self.driver.current_url, page.fav_block.FILMS_BUTTON_URL)

    def test_series_button(self):
        page.fav_block.click_series_button()
        self.assertEqual(self.driver.current_url, page.fav_block.SERIES_BUTTON_URL)
    """

    """
    def test_choose_buttons(self):
        page = FavoritesPage(self.driver)
        page.open()

        page.fav_block.click_choose_films_button()
        self.assertEqual(self.driver.current_url, page.fav_block.CHOOSE_FILMS_BUTTON_URL)

        page.fav_block.click_choose_series_button()
        self.assertEqual(self.driver.current_url, page.fav_block.CHOOSE_SERIES_BUTTON_URL)
    """

    def test_add_film(self):
        page = FavoritesPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.open()
        base_page.main_header.login()
        page.open()

        page.fav_block.add_or_remove_film()
        page.open()

        # page.fav_block.click_series_button()
        # self.assertEqual(self.driver.current_url, page.fav_block.SERIES_BUTTON_URL)

        # page.fav_block.click_films_button()
        # self.assertEqual(self.driver.current_url, page.fav_block.FILMS_BUTTON_URL)

        page.fav_block.add_or_remove_film()
        # assert

    def test_film_block(self):
        base_page = BasePage(self.driver)
        base_page.open()
        base_page.main_header.login()

        page = FavoritesPage(self.driver)
        page.open()
        # check if list is empty
        page.fav_block.add_or_remove_film()
        page.open()

        page.fav_block.click_film_title()
        self.assertEqual(self.driver.current_url, page.fav_block.TEST_FILM_URL)

        page.fav_block.click_film_img()
        self.assertEqual(self.driver.current_url, page.fav_block.TEST_FILM_URL)

        page.fav_block.click_film_city()
        self.assertEqual(self.driver.current_url, page.fav_block.FILM_CITY_URL)

        page.fav_block.click_film_year()
        self.assertEqual(self.driver.current_url, page.fav_block.FILM_YEAR_URL)

        page.fav_block.click_film_drama()
        self.assertEqual(self.driver.current_url, page.fav_block.DRAMA_BUTTON_URL)

        page.fav_block.click_film_comedy()
        self.assertEqual(self.driver.current_url, page.fav_block.COMEDY_BUTTON_URL)

        page.fav_block.click_film_bio()
        self.assertEqual(self.driver.current_url, page.fav_block.BIO_BUTTON_URL)

        page.fav_block.click_film_img()
        self.assertEqual(self.driver.current_url, page.fav_block.TEST_FILM_URL)

        page.fav_block.add_or_remove_film()
        page.open()
        # assert


    """
    def test_login(self):
        page = BasePage(self.driver)
        page.open()
        page.main_header.login()
        # self.assertEqual(self.driver.current_url, page.fav_block.FILMS_BUTTON_URL)
    """






