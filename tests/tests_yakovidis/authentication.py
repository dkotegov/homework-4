import os
import unittest
from tests.pages.auth_page import AuthPage
from tests.pages.profile_page import ProfilePage

from selenium.webdriver import DesiredCapabilities, Remote

from selenium.webdriver.support.ui import WebDriverWait


class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.login = os.environ.get('ADMIN_LOGIN')
        self.password = os.environ.get('ADMIN_PASSWORD')

        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.auth_page = AuthPage(self.driver)
        self.auth_page.open()

        self.auth_form = self.auth_page.auth_form

    def test_wrong_phone_characters(self):
        self.auth_form.wait_visible()
        self.auth_form.set_phone('symbols')
        error = self.auth_form.get_phone_error()

        self.assertEqual(error, 'Обязательное поле', 'nice')

    def test_wrong_length_password(self):
        self.auth_form.wait_visible()
        self.auth_form.set_password('123456')
        error = self.auth_form.get_password_error()

        self.assertEqual(error, 'Минимальная длина: 7', 'nice')

    def auth(self):
        self.auth_page.auth(self.login, self.password)

        profile = ProfilePage(self.driver)
        profile.open()
        profile.wait_open()

        profile.profile_form.logout()

        WebDriverWait(self.driver, 5).until(
            lambda d: d.current_url != 'http://skydelivery.site/'
        )

        self.assertEqual(self.driver.current_url, 'http://skydelivery.site/')

    def tearDown(self):
        self.driver.quit()
