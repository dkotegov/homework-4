# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import MainPage
from tests.common import getDriver, Auth


class AuthTest(unittest.TestCase):
    USERNAME = u'Феофан Лампер'

    def setUp(self):
        self.driver = getDriver()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        Auth(self.driver).sign_in()

        main_page = MainPage(self.driver)
        username = main_page.left_menu.get_username()

        self.assertEqual(self.USERNAME, username)
