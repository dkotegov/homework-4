import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage


class JoinPageTest(unittest.TestCase):
    profile_page = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def tearDown(self):
        self.driver.quit()


'''
    def test_success_join(self):
        name = 'Tim'
        surname = 'Razumov'
        login = os.environ.get('REG_LOGIN')
        password = os.environ.get('REG_PASSWORD')

        self.join_page.join(name, surname, login, password, password)

        nickname = self.join_page.main_header.get_nickname()
        self.assertEqual(login, nickname)
'''
