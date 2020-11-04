import os
import unittest
from tests.pages.profile_page import ProfilePage
from tests.pages.auth_page import AuthPage
from tests.pages.registration_page import RegistrationPage
from tests.helpers.local_storage import LocalStorage

from selenium.webdriver import DesiredCapabilities, Remote


class RegistrationTest(unittest.TestCase):
    DEFAULT_PHOTO = 'data/test_prod_photo.jpg'
    PROFILE_PHOTO = 'data/test_rest_photo.jpg'
    BIG_PROFILE_PHOTO = 'data/test_big_photo.jpg'
    WRONG_PROFILE_PHOTO = 'data/test_non_photo_file'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.registration_page = RegistrationPage(self.driver)
        self.registration_page.open()

        self.registration_form = self.registration_page.registration_form

    def test_wrong_name_and_surname(self):
        self.registration_form.wait_open()
        self.registration_form.set_name('abc')
        self.registration_form.set_surname('abc')

        name_error = self.registration_form.get_name_error()
        surname_error = self.registration_form.get_surname_error()

        self.assertEqual(name_error, 'Минимальная длина: 4')
        self.assertEqual(surname_error, 'Минимальная длина: 4')

    def test_wrong_phone_characters(self):
        self.registration_form.wait_open()
        self.registration_form.set_phone('symbols')
        error = self.registration_form.get_phone_error()

        self.assertEqual(error, 'Обязательное поле', 'nice')

    def test_wrong_length_password(self):
        self.registration_form.wait_open()
        self.registration_form.set_password1('123456')
        error = self.registration_form.get_password1_error()

        self.assertEqual(error, 'Минимальная длина: 7', 'nice')

    def test_password_confirmation(self):
        self.registration_form.wait_open()

        self.registration_form.set_name('asdasdasd')
        self.registration_form.set_surname('asdasdasd')
        self.registration_form.set_phone('89999999999')
        self.registration_form.set_password1('1234567')
        self.registration_form.set_password2('12345678')

        self.registration_form.register()

        confirm_error = self.registration_form.get_confirm_error()

        self.assertEqual(confirm_error, 'Пароли должны совпадать')

    def test_success_registration(self):
        self.registration_form.wait_open()

        self.registration_form.set_name('asdasdasd')
        self.registration_form.set_surname('asdasdasd')
        self.registration_form.set_phone('89999999988')
        self.registration_form.set_password1('1234567')
        self.registration_form.set_password2('1234567')

        self.registration_form.register()

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/me')

    def tearDown(self):
        self.driver.quit()
