from pages.change_password_page import ChangePasswordPage
from pages.profile_page import ProfilePage
from pages.auth_page import AuthPage

from tests.base_test import BaseTest

import settings as s


class ChangePasswordTest(BaseTest):
    BAD_PASSWORD = 'qw12'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_page = AuthPage(cls.driver)

    def setUp(self) -> None:
        self.auth_page.auth()
        self.page = ChangePasswordPage(self.driver, s.USERNAME)
        self.page.open()

    def tearDown(self) -> None:
        self.driver.delete_all_cookies()

    def test_back_btn(self):
        self.page.click_back_btn()

        profile_page = ProfilePage(self.driver)
        self.assertEqual(profile_page.is_opened(), True)

    def test_empty_old_password(self):
        self.page.set_old_password('')
        self.page.set_new_password(s.PASSWORD)
        self.page.set_confirm_password(s.PASSWORD)
        self.page.click_change_btn()

        err = self.page.get_old_password_error()
        self.assertNotEqual(len(err), 0)

    def test_empty_new_password(self):
        self.page.set_old_password(s.PASSWORD)
        self.page.set_new_password('')
        self.page.set_confirm_password(s.PASSWORD)
        self.page.click_change_btn()

        err = self.page.get_new_password_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_password(self):
        self.page.set_old_password(s.PASSWORD)
        self.page.set_new_password(self.BAD_PASSWORD)
        self.page.set_confirm_password(s.PASSWORD)
        self.page.click_change_btn()

        err = self.page.get_new_password_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_password_confirmation(self):
        self.page.set_old_password(s.PASSWORD)
        self.page.set_new_password(s.PASSWORD)
        self.page.set_confirm_password(s.PASSWORD + 'wolf')
        self.page.click_change_btn()

        err = self.page.get_confirm_password_error()
        self.assertNotEqual(len(err), 0)

    def test_change_password(self):
        self.page.set_old_password(s.PASSWORD)
        self.page.set_new_password(s.PASSWORD)
        self.page.set_confirm_password(s.PASSWORD)
        self.page.click_change_btn()

        profile_page = ProfilePage(self.driver)
        self.assertEqual(profile_page.is_opened(), True)
