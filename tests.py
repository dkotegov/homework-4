import os
import unittest
from pages.auth_page import AuthPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class Tests(unittest.TestCase):
    USEREMAIL = 'chuvashov.egor@mail.ru'
    PASSWORD = os.environ['PASSWORD']

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

        auth_form = auth_page.form

        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
        auth_form.open_writing_letter()
