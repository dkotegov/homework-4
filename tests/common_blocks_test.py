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
    def test_click_logo(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.main_header.click_logo()
        self.assertEqual(self.driver.current_url, self.page.main_header.BASE_URL)

    def test_click_recommended(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.main_header.click_recommended()
        self.assertEqual(self.driver.current_url, self.page.main_header.RECOMMENDED_URL)

    def test_click_favorites(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.main_header.click_favorites()
        self.assertEqual(self.driver.current_url, self.page.main_header.FAVORITES_URL)

    def test_click_ratings(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.main_header.click_ratings()
        self.assertEqual(self.driver.current_url, self.page.main_header.RATINGS_URL)

    def test_click_cinema(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_URL)

    def test_click_series(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_URL)

    def test_click_tvshow(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tvshow()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_URL)

    def test_click_tv(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_URL)

    def test_click_stars(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_stars()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_URL)

    def test_click_kinoafisha(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_kinoafisha()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['KINOAFISHA'])

    def test_click_cinema_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['ONLINE'])

    def test_click_cinema_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['TOP'])

    def test_click_cinema_soon(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_soon()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['SOON'])

    def test_click_cinema_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['SELECTIONS'])

    def test_click_cinema_awards(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_awards()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['AWARDS'])

    def test_click_cinema_places(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_places()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['PLACES'])

    def test_click_cinema_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_cinema_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.CINEMA_DROPDOWN_URLS['ARTICLES'])

    def test_click_series_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['TOP'])

    def test_click_series_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ONLINE'])

    def test_click_series_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['SELECTIONS'])

    def test_click_series_all(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series_all()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ALL'])

    def test_click_series_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_series_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.SERIES_DROPDOWN_URLS['ARTICLES'])

    def test_click_tvshow_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tvshow_top()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['TOP'])

    def test_click_tvshow_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tvshow_online()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ONLINE'])

    def test_click_tvshow_all(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tvshow_all()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ALL'])

    def test_click_tvshow_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tvshow_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TVSHOW_DROPDOWN_URLS['ARTICLES'])

    def test_click_tv_central(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv_central()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['CENTRAL'])

    def test_click_tv_local(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv_local()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['LOCAL'])

    def test_click_tv_sport(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv_sport()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['SPORT'])

    def test_click_tv_movies_and_series(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv_movies_and_series()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['MOVIES_SERIES'])

    def test_click_tv_news(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_tv_news()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.TV_DROPDOWN_URLS['NEWS'])

    def test_click_stars_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_stars_articles()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['ARTICLES'])

    def test_click_stars_birthday(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_stars_birthday()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['BIRTHDAY'])

    def test_click_stars_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.nav_bar.click_stars_selections()
        self.assertEqual(self.driver.current_url, self.page.nav_bar.STARS_DROPDOWN_URLS['SELECTIONS'])

    def test_click_cinema(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_cinema()
        self.assertEqual(self.driver.current_url, self.page.footer.CINEMA_URL)

    def test_click_kinoafisha(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_kinoafisha()
        self.assertEqual(self.driver.current_url, self.page.footer.KINOAFISHA_URL)

    def test_click_cinema_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_cinema_online()
        self.assertEqual(self.driver.current_url, self.page.footer.CINEMA_ONLINE_URL)

    def test_click_cinema_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_cinema_top()
        self.assertEqual(self.driver.current_url, self.page.footer.CINEMA_TOP_URL)

    def test_click_soon(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_soon()
        self.assertEqual(self.driver.current_url, self.page.footer.SOON_URL)

    def test_click_cinema_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_cinema_selections()
        self.assertEqual(self.driver.current_url, self.page.footer.CINEMA_SELECTIONS_URL)

    def test_click_awards(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_awards()
        self.assertEqual(self.driver.current_url, self.page.footer.AWARDS_URL)

    def test_click_cinema_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_cinema_articles()
        self.assertEqual(self.driver.current_url, self.page.footer.CINEMA_ARTICLES_URL)

    def test_click_series(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_URL)

    def test_click_series_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series_top()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_TOP_URL)

    def test_click_series_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series_online()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_ONLINE_URL)

    def test_click_series_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series_selections()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_SELECTIONS_URL)

    def test_click_series_all(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series_all()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_ALL_URL)

    def test_click_series_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_series_articles()
        self.assertEqual(self.driver.current_url, self.page.footer.SERIES_ARTICLES_URL)

    def test_click_tvshow(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tvshow()
        self.assertEqual(self.driver.current_url, self.page.footer.TVSHOW_URL)

    def test_click_tvshow_top(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tvshow_top()
        self.assertEqual(self.driver.current_url, self.page.footer.TVSHOW_TOP_URL)

    def test_click_tvshow_top_online(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tvshow_top_online()
        self.assertEqual(self.driver.current_url, self.page.footer.TVSHOW_TOP_ONLINE_URL)

    def test_click_tvshow_top_all(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tvshow_top_all()
        self.assertEqual(self.driver.current_url, self.page.footer.TVSHOW_TOP_ALL_URL)

    def test_click_tvshow_top_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tvshow_top_articles()
        self.assertEqual(self.driver.current_url, self.page.footer.TVSHOW_TOP_ARTICLES_URL)

    def test_click_tv(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tv()
        self.assertEqual(self.driver.current_url, self.page.footer.TV_URL)

    def test_click_tv_central(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_tv_central()
        self.assertEqual(self.driver.current_url, self.page.footer.TV_CENTRAL_URL)

    def test_click_stars(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_stars()
        self.assertEqual(self.driver.current_url, self.page.footer.STARS_URL)

    def test_click_star_articles(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_star_articles()
        self.assertEqual(self.driver.current_url, self.page.footer.STAR_ARTICLES_URL)

    def test_click_star_birthday(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_star_birthday()
        self.assertEqual(self.driver.current_url, self.page.footer.STAR_BIRTHDAY_URL)

    def test_click_star_selections(self):
        self.page = BasePage(self.driver)
        self.page.open()
        self.page.footer.click_star_selections()
        self.assertEqual(self.driver.current_url, self.page.footer.STAR_SELECTIONS_URL)
