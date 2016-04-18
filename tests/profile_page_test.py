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


class ProfilePageTestCase(BaseTestCase):
    def test_upper_block(self):
        page = ProfilePage(self.driver)
        page.open()

        page.profile_block.click_about()
        self.assertEqual(self.driver.current_url, page.profile_block.ABOUT_URL)

        page.profile_block.click_bio()
        self.assertEqual(self.driver.current_url, page.profile_block.BIO_URL)

        page.profile_block.click_films()
        self.assertEqual(self.driver.current_url, page.profile_block.FILMS_URL)

        page.profile_block.click_news()
        self.assertEqual(self.driver.current_url, page.profile_block.NEWS_URL)

    def test_middle_block(self):
        page = ProfilePage(self.driver)
        page.open()

        page.profile_block.click_fishes()
        # self.assertEqual(self.driver.current_url, page.profile_block.FISHES_URL) # _blank
        page.open()

        page.profile_block.click_wiki()
        # self.assertEqual(self.driver.current_url, page.profile_block.WIKI_URL) # _blank
        page.open()

    def test_film_block(self):
        page = ProfilePage(self.driver)
        page.open()

        page.profile_block.click_title()
        self.assertEqual(self.driver.current_url, page.profile_block.FILM_TITLE_URL)
        page.open()

        page.profile_block.click_year()
        self.assertEqual(self.driver.current_url, page.profile_block.FILM_YEAR_URL)
        page.open()

        page.profile_block.click_country()
        self.assertEqual(self.driver.current_url, page.profile_block.FILM_COUNTRY_URL)
        page.open()

        page.profile_block.click_rezh()
        self.assertEqual(self.driver.current_url, page.profile_block.FILM_REZH_URL)
        page.open()

        page.profile_block.click_role()
        self.assertEqual(self.driver.current_url, page.profile_block.FILM_ROLE_URL)
        page.open()

    def test_lower_block(self):
        page = ProfilePage(self.driver)
        page.open()

        page.profile_block.click_all_films()
        self.assertEqual(self.driver.current_url, page.profile_block.ALL_FILMS_URL)
        page.open()

        page.profile_block.click_article()
        self.assertEqual(self.driver.current_url, page.profile_block.ARTICLE_URL)
        page.open()

        page.profile_block.click_born_today()
        self.assertEqual(self.driver.current_url, page.profile_block.BORN_TODAY_URL)
        page.open()

        page.profile_block.click_star_news()
        self.assertEqual(self.driver.current_url, page.profile_block.STAR_NEWS_URL)
        page.open()

        page.profile_block.click_all_star_news()
        self.assertEqual(self.driver.current_url, page.profile_block.STAR_NEWS_URL)
        page.open()



