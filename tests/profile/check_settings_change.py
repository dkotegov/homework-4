import unittest

from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckSettingsChange(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)

        self.profile_page = ProfilePage(self.driver)
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def test_open_settings(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        is_auth = self.main_page.check_auth()
        self.assertTrue(is_auth)
        self.profile_page.open()
        self.profile_page.click_settings_form_button()
        is_settings_open = self.profile_page.check_settings_form_open()
        self.assertTrue(is_settings_open)

    def test_change_login(self):
        self.test_open_settings()
        self.profile_page.change_login(self.EMAIL + "123")
        is_error = self.profile_page.check_login_changed(self.EMAIL + "123")
        self.assertTrue(is_error)

    def test_change_email(self):
        self.test_open_settings()
        self.profile_page.change_email(self.EMAIL, self.EMAIL + "abc")
        is_error = self.profile_page.check_email_changed(self.EMAIL + "abc")
        self.profile_page.change_email(self.EMAIL + "abc", self.EMAIL)
        self.assertTrue(is_error)

    def test_change_email_exist(self):
        self.test_open_settings()
        self.profile_page.change_email(self.EMAIL, "Alkirys1@mail.ru")
        is_error = self.profile_page.check_error_with_text("Данный Email адрес уже существует")
        self.assertTrue(is_error)

    def test_change_email_wrong_format(self):
        self.test_open_settings()
        self.profile_page.change_email(self.EMAIL, "Alkirys@mail.ruAlkirys@mail.ru")
        is_error = self.profile_page.check_error_with_text("Неправильный формат E-mail")
        self.assertTrue(is_error)

    def test_click_safety_button(self):
        self.test_open_settings()
        self.profile_page.click_safety_button()
        is_clicked = self.profile_page.check_safety_button_clicked()
        self.assertTrue(is_clicked)

    def test_change_password(self):
        self.test_click_safety_button()
        self.profile_page.change_password(self.PASSWORD, self.PASSWORD + "s")
        self.profile_page.click_info_button()
        self.profile_page.click_safety_button()
        self.profile_page.submit_form()
        is_error = self.profile_page.check_error_with_text("Неверный пароль")
        self.assertTrue(is_error)

        self.profile_page.open()
        self.profile_page.click_settings_form_button()
        is_settings_open = self.profile_page.check_settings_form_open()
        self.assertTrue(is_settings_open)
        self.profile_page.click_safety_button()
        self.profile_page.check_safety_button_clicked()

        self.profile_page.change_password(self.PASSWORD + "s", self.PASSWORD)

    def test_password_short_error(self):
        self.test_click_safety_button()
        self.profile_page.change_new_password("123")
        self.profile_page.submit_form()
        is_error = self.profile_page.check_error_with_text("Пароль должен содержать не менее 6 символов")
        self.assertTrue(is_error)

    def test_upload_avatar(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        self.main_page.check_auth()
        self.profile_page.open()
        result = self.profile_page.check_changing_avatar()
        self.assertTrue(result)

    def test_passwords_different(self):
        self.test_click_safety_button()
        self.profile_page.change_new_password("12334467456")
        self.profile_page.change_again_password("122343434")
        self.profile_page.submit_form()
        is_error = self.profile_page.check_error_with_text("Пароли не совпадают")
        self.assertTrue(is_error)

    def test_settings_close(self):
        self.test_open_settings()
        self.profile_page.click_close_button()
        is_closed = self.profile_page.check_close_clicked()
        self.assertTrue(is_closed)

    def test_subscription(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        is_auth = self.main_page.check_auth()
        self.assertTrue(is_auth)
        self.profile_page.open()
        self.profile_page.click_subscription_button()
        is_closed = self.profile_page.check_umoney_redirected()
        self.assertTrue(is_closed)

    def tearDown(self):
        self.driver.quit()
