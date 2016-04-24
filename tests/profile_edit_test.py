import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages import AuthPage


class ProfileEditTestCase(unittest.TestCase):
    USEREMAIL = 'smirnova.a.yu@mail.ru'
    USERPASSWORD = os.environ.get('HW4PASSWORD')

    def setUp(self):
        self.browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.USERPASSWORD)
        auth_form.submit()
        pass