import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.personal_data.src.main_page import MainPage
from tests.personal_data.src.auth_page import AuthPage


class MainTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        # browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def authorize(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)
        auth_page.top_menu.get_username()

    def test_redirect_contacts(self):
        self.authorize()

        main_page = MainPage(self.driver)
        main_page.open()

        main_page.form.open_contacts()
        main_page.form.check_contacts_opened()

    def test_redirect_personal_data(self):
        self.authorize()

        main_page = MainPage(self.driver)
        main_page.open()

        main_page.form.open_personal_data()
        main_page.form.check_personal_data_opened()
