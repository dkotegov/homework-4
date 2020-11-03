# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
from Auth import AuthPage
from Home import HomePage


class TabsAtHomePageTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_box(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_inbox()

    def test_select_files(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.select_all_files()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_helper(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_helper()

    def test_open_share(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_share_button()
