# -*- coding: utf-8 -*-
import os
import unittest

import utils
from Auth import AuthPage
from Home import HomePage


class TabsAtHomePageTest(unittest.TestCase):
    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = utils.get_remote_driver(browser)

        LOGIN = 'alexersh.testing'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_box(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.open_inbox()

    def test_select_files(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.select_all_files()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_helper(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.open_helper()

    def test_open_share(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.utils.close_banner_if_exists()
        home_page.tabs_at_home_p.open_share_button()
