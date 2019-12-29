import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage


class BasicTest(unittest.TestCase):
    MAIL_URL = 'https://e.mail.ru/inbox'
    LOGIN_URL = 'https://account.mail.ru/login'
    SIGNUP_URL = 'https://account.mail.ru/signup'
    AUTH_URL = 'https://e.mail.ru/login'
    auth_frame = 'ag-popup__frame__layout__iframe'

    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER)
        else:
            # Selenium Grig in development
            nodeURL = 'http://localhost:4444/wd/hub'
            capabilities = DesiredCapabilities.chrome()
            capabilities.setBrowserName("chrome")
            capabilities.setVersion("79")

            self.driver = Remote(
                command_executor=nodeURL,
                desired_capabilities=getattr(
                    DesiredCapabilities, config.DEFAULT_BROWSER).copy()
            )

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.wait_redirect(self.AUTH_URL)
        login_page.open_iframe(self.auth_frame)
        login_page.sign_in(self.login, self.password)
