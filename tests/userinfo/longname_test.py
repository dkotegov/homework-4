import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage
from pages.userinfo_page import UserinfoPage

class LongSurnameTest(unittest.TestCase):
    LONG_SURNAME = f'{"very" * 10} long'
    TOP_MESSAGE = 'Некоторые поля заполнены неверно'
    SURNAME_ERROR = 'Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов.'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.authorize()

        userinfo_page = UserinfoPage(self.driver)
        userinfo_page.open()
        userinfo_form = userinfo_page.form
        userinfo_form.set_surname(self.LONG_SURNAME)
        userinfo_form.save()
        self.assertEqual(self.TOP_MESSAGE, userinfo_form.get_top_message())
        self.assertEqual(self.SURNAME_ERROR, userinfo_form.get_surname_message())