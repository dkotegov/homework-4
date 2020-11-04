import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.main import MainPage
from steps.auth import AuthSteps


# Вход в конструктор
class AuthTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    WRONG_KEY = '1234'
    AUTH_SUCCESS = 'Правильный ключ'
    AUTH_FAILED = 'Ошибка'
    wrong_keys = [WRONG_KEY, ""]

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='127.17.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        auth_page = AuthSteps(self.driver)
        auth_page.open()
        auth_page.login(self.KEY)
        to = MainPage.BASE_URL + MainPage.PATH
        auth_page.do_redirect(to)
        self.assertEqual(self.driver.current_url, to)

    def test_login_failed(self):
        for key in self.wrong_keys:
            with self.subTest():
                auth_page = AuthSteps(self.driver)
                auth_page.open()
                alert_text = auth_page.login(key)
                self.assertEqual(alert_text, self.AUTH_FAILED)
