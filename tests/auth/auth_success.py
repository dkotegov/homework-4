import os

import unittest
from tests.default_setup import default_setup
from Pages.auth_page import AuthPage
from steps.get_profile_login import get_profile_login


class AuthTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.open()

    def tearDown(self):
        self.auth_page.logout()
        self.driver.quit()

    def test_auth_success(self):
        self.auth_page.set_login(self.LOGIN)
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        self.auth_page.wait_auth()
        current_login = get_profile_login(self)
        self.assertEqual(self.LOGIN, current_login)


    '''def test_auth_wrong_login(self):
        auth_page = AuthPage(self.driver)
        password = os.environ['PASSWORD']
        auth_page.auth_wrong("xmksamxsmlksa", password)

    def test_auth_wrong_password(self):
        auth_page = AuthPage(self.driver)
        login = os.environ['LOGIN']
        auth_page.auth_wrong(login, "ofcspslaxx")

    def test_auth_clear(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth_wrong("", "")

    def test_logout(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        auth_page.logout()
'''