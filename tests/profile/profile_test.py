import os
from random import randrange

from pages.profile_page import ProfilePage
from pages.auth_page import AuthPage
from pages.change_password_page import ChangePasswordPage
from pages.main_page import MainPage

from tests.base_test import BaseTest

import settings as s


class ProfileTest(BaseTest):
    auth_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_page = AuthPage(cls.driver)

    def setUp(self) -> None:
        self.auth_page.auth()
        self.page = ProfilePage(self.driver)
        self.page.open()

    def tearDown(self):
        self.driver.delete_all_cookies()

    def test_good_avatar(self):
        if not self.page.is_windows():
            return

        old_avatar_url = self.page.get_avatar_url()

        avatar_path = os.path.join(os.getcwd(), 'images', 'good_avatar.png')
        self.page.send_file(self.page.click_avatar, avatar_path)

        self.assertTrue('success' in self.page.get_popup().get_attribute('class'))

        self.page.wait_until(lambda d: self.page.get_avatar_url() != old_avatar_url)
        new_avatar_dataurl = self.page.get_avatar_url()
        self.assertNotEqual(old_avatar_url, new_avatar_dataurl)

        # avatar image initially changes to dataurl and only after refresh - to real url
        self.driver.refresh()
        new_avatar_url = self.page.get_avatar_url()

        self.assertNotEqual(old_avatar_url, new_avatar_url)

    def test_incorrect_email_error(self):
        self.page.set_email('wolf@wolf')
        self.page.click_save_btn()
        err = self.page.get_email_error()
        self.assertNotEqual(len(err), 0)

    def test_name_and_email_change(self):
        # [] to prevent from specifying real liokor.ru user
        new_email = 'wolf[{}]@liokor.ru'.format(randrange(0, 1024))
        new_name = 'Wolf{}'.format(randrange(0, 1024))

        self.page.set_email(new_email)
        self.page.set_name(new_name)
        self.page.click_save_btn()
        self.assertTrue('success' in self.page.get_popup().get_attribute('class'))

        # to check that server really changed data - refreshing page and checking
        self.driver.refresh()

        self.assertEqual(new_email, self.page.get_email())
        self.assertEqual(new_name, self.page.get_name())

    def test_change_password_btn(self):
        self.page.click_change_password_btn()

        change_password_page = ChangePasswordPage(self.driver, s.USERNAME)
        self.assertEqual(change_password_page.is_opened(), True)

    def test_back_btn(self):
        self.page.click_back_btn()

        main_page = MainPage(self.driver)
        self.assertEqual(main_page.is_opened(), True)

    def test_logout(self):
        self.page.click_logout_btn()

        self.assertEqual(self.auth_page.is_opened(), True)

        # check redirect back to auth
        self.page.open()
        self.assertEqual(self.auth_page.is_opened(), True)
