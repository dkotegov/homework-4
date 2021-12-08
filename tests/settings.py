from pages.login import LoginPage
from pages.profile import ProfilePage
from pages.settings import SettingsPage
from tests.base import BaseTest
from os import environ

from utils.helpers import wait_for_visible


class SettingsTestSuite(BaseTest):
    def test_empty_email(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_info(email='')
        settings.submit_change_info()

        self.assertEqual('Некорректный формат Email', settings.email_error_hint)

    def test_password_only_digits(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_info(password='1234567890', confirm_password='1234567890')
        settings.submit_change_info()

        self.assertEqual('Пароль должен содержать хотя бы одну букву!', settings.password_error_hint)

    def test_password_only_letters(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_info(password='abcdefghij', confirm_password='abcdefghij')
        settings.submit_change_info()

        self.assertEqual('Пароль должен содержать хотя бы одну цифру!', settings.password_error_hint)

    def test_not_matching_passwords(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_info(password='newpassword1', confirm_password='newpassword2')
        settings.submit_change_info()

        self.assertEqual('Пароли не совпадают!', settings.password_error_hint)

    def test_changing_email(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_info(email='newemail@mail.ru')
        settings.submit_change_info()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        try:
            self.assertEqual(f'{settings.ROOT_URL}/user/{environ["LOGIN"]}', self.driver.current_url)
        finally:
            # reverting changes made
            settings.open()
            settings.change_info(email=environ['EMAIL'])
            settings.submit_change_info()

    def test_upload_valid_avatar(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        settings.change_avatar('new_avatar.png')
        settings.submit_change_avatar()
        settings.reload()
        new_src = settings.avatar_img_src

        try:
            profile = ProfilePage(self.driver)
            profile.open()
            wait_for_visible(self.driver, login.USER_NAME_HEADER)
            self.assertEqual(new_src, profile.avatar_img_src)
        finally:
            # reverting changes made
            settings.open()
            settings.change_avatar('default_avatar.jpeg')
            settings.submit_change_avatar()

    def test_upload_avatar_wrong_extension(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        old_src = settings.avatar_img_src
        settings.change_avatar('avatar_wrong.txt')
        hint = settings.avatar_error_hint
        new_src = settings.avatar_img_src

        self.assertEqual('Некорректный формат картинки! Используйте png или jpeg', hint)
        self.assertEqual(old_src, new_src)

    def test_upload_avatar_exceeds_size(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        settings.open()
        old_src = settings.avatar_img_src
        settings.change_avatar('heavy_image.jpg')
        hint = settings.avatar_error_hint
        new_src = settings.avatar_img_src

        self.assertEqual('Размер файла не должен превышать 5MB!', hint)
        self.assertEqual(old_src, new_src)
