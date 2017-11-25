# -*- coding: utf-8 -*-

from like_tests.tests.base import BaseTest
from like_tests.elements.user.pages import UserPage


class AuthTests(BaseTest):

    def test_login(self):
        self.assertEqual(UserPage.USER_NAME1, self.user_page.user_header.get_username())

    def test_logout(self):
        self.user_page.logout()
        logged_in = self.user_page.is_logged_out()
        self.assertTrue(logged_in)