# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import BasePage
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = BasePage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()


class CommonBlocksTestCase(BaseTestCase):

    def test_main_header(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.main_header.click_logo()
        self.assertEqual(self.driver.current_url, self.page.main_header.BASE_URL)

        self.page.main_header.click_recommended()
        self.assertEqual(self.driver.current_url, self.page.main_header.RECOMMENDED_URL)

        self.page.main_header.click_favorites()
        self.assertEqual(self.driver.current_url, self.page.main_header.FAVORITES_URL)

        self.page.main_header.click_ratings()
        self.assertEqual(self.driver.current_url, self.page.main_header.RATINGS_URL)

    def test_nav_bar(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_cinema()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_URL)

        self.page.nav_bar.click_series()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_URL)

        self.page.nav_bar.click_tvshow()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_URL)

        self.page.nav_bar.click_tv()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_URL)

        self.page.nav_bar.click_stars()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_URL)

    def test_cinema_dropdown(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_kinoafisha()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['KINOAFISHA'])

        self.page.nav_bar.click_cinema_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['ONLINE'])

        self.page.nav_bar.click_cinema_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['TOP'])

        self.page.nav_bar.click_cinema_soon()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['SOON'])

        self.page.nav_bar.click_cinema_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['SELECTIONS'])

        self.page.nav_bar.click_cinema_awards()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['AWARDS'])

        self.page.nav_bar.click_cinema_places()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['PLACES'])

        self.page.nav_bar.click_cinema_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['ARTICLES'])

    def test_series_dropdown(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_series_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['TOP'])

        self.page.nav_bar.click_series_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ONLINE'])

        self.page.nav_bar.click_series_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['SELECTIONS'])

        self.page.nav_bar.click_series_all()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ALL'])

        self.page.nav_bar.click_series_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ARTICLES'])

    def test_tvshow_dropdown(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_tvshow_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['TOP'])

        self.page.nav_bar.click_tvshow_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ONLINE'])

        self.page.nav_bar.click_tvshow_all()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ALL'])

        self.page.nav_bar.click_tvshow_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ARTICLES'])

    def test_tvprogramm_dropdown(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_tv_central()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['CENTRAL'])

        self.page.nav_bar.click_tv_local()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['LOCAL'])

        self.page.nav_bar.click_tv_sport()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['SPORT'])

        self.page.nav_bar.click_tv_movies_and_series()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['MOVIES_SERIES'])

        self.page.nav_bar.click_tv_news()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['NEWS'])

    def test_stars_dropdown(self):
        # self.page = BasePage(self.driver)
        # self.page.open()

        self.page.nav_bar.click_stars_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['ARTICLES'])

        self.page.nav_bar.click_stars_birthday()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['BIRTHDAY'])

        self.page.nav_bar.click_stars_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['SELECTIONS'])

