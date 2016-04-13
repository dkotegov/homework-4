# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities

from pages.pages import ActorProfilePage
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


class MainHeaderTestCase(BaseTestCase):
    def test_links_behaviour(self):
        self.page = ActorProfilePage(self.driver)
        self.page.open()
        self.page.main_header.click_subheader('CINEMA')
        self.assertEqual(self.driver.current_url, self.page.main_header.cinema_href)
        self.page.main_header.click_subheader('SERIES')
        self.assertEqual(self.driver.current_url, self.page.main_header.series_href)
        self.page.main_header.click_subheader('TV_SHOWS')
        self.assertEqual(self.driver.current_url, self.page.main_header.shows_href)
        self.page.main_header.click_subheader('TV_PROGRAM')
        self.assertEqual(self.driver.current_url, self.page.main_header.programs_href)
        self.page.main_header.click_subheader('STARS')
        self.assertEqual(self.driver.current_url, self.page.main_header.stars_href)

    def test_dropdown_behaviour(self):
        pass
