from pages.change_password_page import ChangePasswordPage
from pages.profile_page import ProfilePage
from pages.auth_page import AuthPage

from tests.base_test import BaseTest

import settings as s


class ChangePasswordTest(BaseTest):
    BAD_PASSWORD = 'qw12'
    MIN_PASSWORD = 'qwer123'
    GOOD_PASSWORD = '123412123421superSTRONGp@ssword-wolf-lion-LIOKORRRRRRRR213412341234231_--======1234=1234=1=2='

    current_password = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        auth_page = AuthPage(cls.driver)
        auth_page.auth()

    def setUp(self) -> None:
        self.page = ChangePasswordPage(self.driver, s.USERNAME)
        self.page.open()

    def test_back_btn(self):
        self.page.click_back_btn()

        profile_page = ProfilePage(self.driver)
        self.assertEqual(profile_page.is_opened(), True)

    def _test_change_password(self, old, new):
        profile_page = ProfilePage(self.driver)

        self.page.change_password(s.PASSWORD, self.GOOD_PASSWORD)
        self.assertEqual(profile_page.is_opened(), True)

        # to verify that password really changed
        profile_page.click_change_password_btn()
        self.page.change_password(self.GOOD_PASSWORD, s.PASSWORD)
        self.assertEqual(profile_page.is_opened(), True)

    def test_empty_old_password(self):
        self.page.set_old_password('')
        self.page.set_new_password(s.PASSWORD)
        self.page.set_confirm_password(s.PASSWORD)
        self.page.click_change_btn()

        err = self.page.get_old_password_error()
        self.assertNotEqual(len(err), 0)

    def test_bad_old_password(self):
        self.page.set_old_password(s.PASSWORD + 'wolf')
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

    def test_change_password_min(self):
        self._test_change_password(s.PASSWORD, self.MIN_PASSWORD)

    def test_change_password_good(self):
        self._test_change_password(s.PASSWORD, self.GOOD_PASSWORD)
