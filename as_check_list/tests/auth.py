# -*- coding: utf-8 -*-

from as_check_list.tests.base import BaseTest
from as_check_list.elements.user.pages import UserPage


class AuthTests(BaseTest):
    def test_login(self):
        self.assertEqual(UserPage.USER_NAME1, self.user_page.user_header.get_username())

    def test_logout(self):
        self.user_page.logout()
        logged_in = self.user_page.is_logged_out()
        self.assertTrue(logged_in)
