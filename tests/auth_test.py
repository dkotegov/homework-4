# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Main


class AuthTest(unittest.TestCase):
    USERNAME = u'Феофан Лампер'

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_auth(self):
        Auth(self.driver).sign_in()

        username = Main(self.driver).get_username()
        self.assertEqual(self.USERNAME, username)
