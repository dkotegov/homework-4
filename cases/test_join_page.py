import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.join_page import JoinPage
from pages.login_page import LoginPage


class JoinPageTest(unittest.TestCase):
    join_page = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.join_page = JoinPage(self.driver)
        self.join_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_success_join(self):
        name = 'Tim'
        surname = 'Razumov'
        login = os.environ.get('REG_LOGIN')
        password = os.environ.get('REG_PASSWORD')

        is_join = self.join_page.join(name, surname, login, password, password)

        self.assertTrue(is_join)

    def test_invalid_name_join(self):
        name = '1'

        self.join_page.join_form.set_name(name)

        is_open = self.join_page.join_form.is_open_invalid_name()
        self.assertTrue(is_open)

    def test_invalid_surname_join(self):
        surname = '1'

        self.join_page.join_form.set_surname(surname)

        is_open = self.join_page.join_form.is_open_invalid_surname()
        self.assertTrue(is_open)

    def test_invalid_login_join(self):
        login = '1'

        self.join_page.join_form.set_login(login)

        is_open = self.join_page.join_form.is_open_invalid_login()
        self.assertTrue(is_open)

    def test_exists_login_join(self):
        name = 'Tim'
        surname = 'Razumov'
        login = name + surname
        password = os.environ.get('REG_PASSWORD')

        is_join = self.join_page.join(name, surname, login, password, password)

        self.assertTrue(not is_join)

    def test_invalid_password_join(self):
        password = '1'

        self.join_page.join_form.set_password(password)

        is_open = self.join_page.join_form.is_open_invalid_password()
        self.assertTrue(is_open)

    def test_invalid_repeat_password_join(self):
        password = os.environ.get('REG_PASSWORD')
        password2 = password + '1'

        self.join_page.join_form.set_password(password)
        self.join_page.join_form.set_password_repeat(password2)
        self.join_page.join_form.submit()

        is_open = self.join_page.join_form.is_open_invalid_password()
        self.assertTrue(is_open)

    def test_empty_inputs_join(self):
        self.join_page.join_form.submit()

        is_open = self.join_page.join_form.is_open_invalid_name()
        self.assertTrue(is_open)

    def test_click_on_login(self):
        self.join_page.join_form.open_login()

        login_form = LoginPage(self.driver).login_form
        self.assertTrue(login_form.is_open)
