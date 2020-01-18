# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage   
from BaseUrls import BaseUrls
class BasicTest(unittest.TestCase, BaseUrls):
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER)
        else:
            # Selenium Grid in development
            nodeURL = 'http://localhost:4444/wd/hub'
            capabilities = DesiredCapabilities.chrome()
            capabilities.setBrowserName("chrome")
            capabilities.setVersion("79")

            self.driver = Remote(
                command_executor=nodeURL,
                desired_capabilities=getattr(
                    DesiredCapabilities, config.DEFAULT_BROWSER).copy()
            )
        self.pre_tests()

    def tearDown(self):
        self.driver.quit()

    def pre_tests(self):
        pass

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.sign_in(self.login, self.password)
        login_page.wait_redirect(self.MAIL_URL)
        
    def auth_another_account(self):
        login_page = LoginPage(self.driver)
        login_page.sign_in_only_password(self.password)
        login_page.wait_redirect(self.MAIL_URL)
