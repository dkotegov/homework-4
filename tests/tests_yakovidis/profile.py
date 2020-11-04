import os
import unittest
from tests.pages.profile_page import ProfilePage
from tests.pages.auth_page import AuthPage

from selenium.webdriver import DesiredCapabilities, Remote


class ProfileTest(unittest.TestCase):
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

        login = os.environ.get('ADMIN_LOGIN')
        password = os.environ.get('ADMIN_PASSWORD')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.wait_open()
        auth_page.auth(login, password)

        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

        self.profile_form = self.profile_page.profile_form

    def test_wrong_name_and_surname(self):
        self.profile_form.wait_open()
        self.profile_form.clear_name()
        self.profile_form.clear_surname()

        self.profile_form.set_name('abc')
        self.profile_form.set_surname('abc')

        name_error = self.profile_form.get_name_error()
        surname_error = self.profile_form.get_surname_error()

        self.assertEqual(name_error, 'Минимальная длина: 4')
        self.assertEqual(surname_error, 'Минимальная длина: 4')

    def test_wrong_email(self):
        self.profile_form.wait_open()
        self.profile_form.set_email('wrong email')

        email_error = self.profile_form.get_email_error()

        self.assertEqual(email_error, 'Неверный формат')

    def test_save_big_photo(self):
        self.profile_form.wait_open()
        self.profile_form.set_photo(self.BIG_PROFILE_PHOTO)

        photo_error = self.profile_form.get_photo_error()

        self.assertEqual(photo_error, 'Максимальный размер файла - 1МБ')

    def test_save_wrong_type_photo(self):
        self.profile_form.wait_open()
        self.profile_form.set_photo(self.WRONG_PROFILE_PHOTO)

        photo_error = self.profile_form.get_photo_error()

        self.assertEqual(photo_error, 'Допустимые форматы: .jpg, .jpeg, .png, .svg')

    def test_update_profile(self):
        self.profile_form.wait_open()

        self.profile_form.clear_all()

        self.profile_form.set_photo(self.PROFILE_PHOTO)
        self.profile_form.set_name('name')
        self.profile_form.set_surname('surname')
        self.profile_form.set_email('email@email.com')

        self.profile_form.save()
        self.driver.refresh()

        self.profile_form.wait_open()

        self.assertEqual(self.profile_form.get_name(), 'name')
        self.assertEqual(self.profile_form.get_surname(), 'surname')
        self.assertEqual(self.profile_form.get_email(), 'email@email.com')

    def tearDown(self):
        self.driver.quit()
