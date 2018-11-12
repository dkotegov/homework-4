import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class Test(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)

        sidebar = main_page.sidebar
        sidebar.create_new_dir()
        sidebar.set_dir_name("Test_Rustam")
        sidebar.submit_new_dir()