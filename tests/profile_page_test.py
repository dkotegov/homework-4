# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import ProfilePage
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.page = ProfilePage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.quit()


class ProfilePageTestCase(BaseTestCase):
    def test_click_about(self):
        self.page.profile_block.click_about()
        self.assertEqual(self.driver.current_url, self.page.profile_block.ABOUT_URL)

    def test_click_bio(self):
        self.page.profile_block.click_bio()
        self.assertEqual(self.driver.current_url, self.page.profile_block.BIO_URL)

    def test_click_films(self):
        self.page.profile_block.click_films()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILMS_URL)

    def test_click_title(self):
        self.page.profile_block.click_title()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILM_TITLE_URL)

    def test_click_year(self):
        self.page.profile_block.click_year()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILM_YEAR_URL)

    def test_click_country(self):
        self.page.profile_block.click_country()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILM_COUNTRY_URL)

    def test_click_rezh(self):
        self.page.profile_block.click_rezh()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILM_REZH_URL)

    def test_click_role(self):
        self.page.profile_block.click_role()
        self.assertEqual(self.driver.current_url, self.page.profile_block.FILM_ROLE_URL)

    def test_click_all_films(self):
        self.page.profile_block.click_all_films()
        self.assertEqual(self.driver.current_url, self.page.profile_block.ALL_FILMS_URL)

    def test_click_article(self):
        self.page.profile_block.click_article()
        self.assertEqual(self.driver.current_url, self.page.profile_block.ARTICLE_URL)

    def test_click_born_today(self):
        self.page.profile_block.click_born_today()
        self.assertEqual(self.driver.current_url, self.page.profile_block.BORN_TODAY_URL)

    def test_click_star_news(self):
        self.page.profile_block.click_star_news()
        self.assertEqual(self.driver.current_url, self.page.profile_block.STAR_NEWS_URL)
