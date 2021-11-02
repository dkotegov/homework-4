from pages.login import LoginPage
from pages.settings import SettingsPage
from tests.base import BaseTest
from os import environ


class SettingsTestSuite(BaseTest):
    def test_empty_email(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        settings.open()
        settings.change_info(email='')
        settings.submit_change_info()

        self.assertEqual('Некорректный формат Email', settings.email_error_hint)

    def test_password_only_digits(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        settings.open()
        settings.change_info(password='1234567890', confirm_password='1234567890')
        settings.submit_change_info()

        self.assertEqual('Пароль должен содержать хотя бы одну букву!', settings.password_error_hint)

    def test_password_only_letters(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        settings.open()
        settings.change_info(password='abcdefghij', confirm_password='abcdefghij')
        settings.submit_change_info()

        self.assertEqual('Пароль должен содержать хотя бы одну цифру!', settings.password_error_hint)

    def test_not_matching_passwords(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        settings.open()
        settings.change_info(password='newpassword1', confirm_password='newpassword2')
        settings.submit_change_info()

        self.assertEqual('Пароли не совпадают!', settings.password_error_hint)

    def test_changing_email(self):
        login = LoginPage(self.driver)
        settings = SettingsPage(self.driver)

        login.open()
        login.sign_in()

        settings.open()
        settings.change_info(email='newemail@mail.ru')
        settings.submit_change_info()

        try:
            self.assertEqual(f'{settings.ROOT_URL}/user/{environ["LOGIN"]}', self.driver.current_url)
        finally:
            # reverting changes made
            settings.open()
            settings.change_info(email=environ['EMAIL'])
            settings.submit_change_info()

    def upload_valid_avatar(self):
        pass

    def upload_avatar_wrong_extension(self):
        pass

    def upload_avatar_exceeds_size(self):
        pass
