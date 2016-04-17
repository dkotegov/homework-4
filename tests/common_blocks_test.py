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

    def tearDown(self):
        self.driver.quit()


class CommonBlocksTestCase(BaseTestCase):

    def test_main_header(self):
        page = BasePage(self.driver)
        page.open()

        page.main_header.click_logo()
        self.assertEqual(self.driver.current_url, page.main_header.BASE_URL)

        page.main_header.click_recommended()
        self.assertEqual(self.driver.current_url, page.main_header.RECOMMENDED_URL)

        page.main_header.click_favorites()
        self.assertEqual(self.driver.current_url, page.main_header.FAVORITES_URL)

        page.main_header.click_ratings()
        self.assertEqual(self.driver.current_url, page.main_header.RATINGS_URL)

    def test_nav_bar(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_cinema()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_URL)

        page.nav_bar.click_series()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_URL)

        page.nav_bar.click_tvshow()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVSHOW_URL)

        page.nav_bar.click_tvprogramm()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVPROGRAMM_URL)

        page.nav_bar.click_stars()
        self.assertEqual(self.driver.current_url, page.nav_bar.STARS_URL)

    def test_cinema_dropdown(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_kinoafisha()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['KINOAFISHA'])

        page.nav_bar.click_cinema_online()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['ONLINE'])

        page.nav_bar.click_cinema_top()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['TOP'])

        page.nav_bar.click_cinema_soon()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['SOON'])

        page.nav_bar.click_cinema_selections()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['SELECTIONS'])

        page.nav_bar.click_cinema_awards()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['AWARDS'])

        page.nav_bar.click_cinema_places()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['PLACES'])

        page.nav_bar.click_cinema_articles()
        self.assertEqual(self.driver.current_url, page.nav_bar.CINEMA_DROPDOWN_URLS['ARTICLES'])

    def test_series_dropdown(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_series_top()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_DROPDOWN_URLS['TOP'])

        page.nav_bar.click_series_online()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_DROPDOWN_URLS['ONLINE'])

        page.nav_bar.click_series_selections()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_DROPDOWN_URLS['SELECTIONS'])

        page.nav_bar.click_series_all()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_DROPDOWN_URLS['ALL'])

        page.nav_bar.click_series_articles()
        self.assertEqual(self.driver.current_url, page.nav_bar.SERIES_DROPDOWN_URLS['ARTICLES'])

    def test_tvshow_dropdown(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_tvshow_top()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVSHOW_DROPDOWN_URLS['TOP'])

        page.nav_bar.click_tvshow_online()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVSHOW_DROPDOWN_URLS['ONLINE'])

        page.nav_bar.click_tvshow_all()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVSHOW_DROPDOWN_URLS['ALL'])

        page.nav_bar.click_tvshow_articles()
        self.assertEqual(self.driver.current_url, page.nav_bar.TVSHOW_DROPDOWN_URLS['ARTICLES'])

    def test_tvprogramm_dropdown(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_tv_central()
        self.assertEqual(self.driver.current_url, page.nav_bar.TV_DROPDOWN_URLS['CENTRAL'])

        page.nav_bar.click_tv_local()
        self.assertEqual(self.driver.current_url, page.nav_bar.TV_DROPDOWN_URLS['LOCAL'])

        page.nav_bar.click_tv_sport()
        self.assertEqual(self.driver.current_url, page.nav_bar.TV_DROPDOWN_URLS['SPORT'])

        page.nav_bar.click_tv_movies_and_series()
        self.assertEqual(self.driver.current_url, page.nav_bar.TV_DROPDOWN_URLS['MOVIES_SERIES'])

        page.nav_bar.click_tv_news()
        self.assertEqual(self.driver.current_url, page.nav_bar.TV_DROPDOWN_URLS['NEWS'])

    def test_stars_dropdown(self):
        page = BasePage(self.driver)
        page.open()

        page.nav_bar.click_stars_articles()
        self.assertEqual(self.driver.current_url, page.nav_bar.STARS_DROPDOWN_URLS['ARTICLES'])

        page.nav_bar.click_stars_birthday()
        self.assertEqual(self.driver.current_url, page.nav_bar.STARS_DROPDOWN_URLS['BIRTHDAY'])

        page.nav_bar.click_stars_selections()
        self.assertEqual(self.driver.current_url, page.nav_bar.STARS_DROPDOWN_URLS['SELECTIONS'])

