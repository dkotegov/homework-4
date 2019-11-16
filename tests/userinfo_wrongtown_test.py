import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage
from pages.userinfo_page import UserinfoPage

class WrongTownTest(unittest.TestCase):
    WRONG_TOWN_NAME = 'qwertyuiop'
    TOP_MESSAGE = 'Некоторые поля заполнены неверно'
    TOWN_ERROR = 'Проверьте название города'

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
        userinfo_form.set_town(self.WRONG_TOWN_NAME)
        userinfo_form.save()
        self.assertEqual(self.TOP_MESSAGE, userinfo_form.get_top_message())
        self.assertEqual(self.TOWN_ERROR, userinfo_form.get_town_message())