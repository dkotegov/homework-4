# -*- coding: utf-8 -*-
from page_objects import *
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def get_evironment():
    name_of_browser_var = 'HW4BROWSER'
    name_of_password_var = 'HW4PASSWORD'
    try:
        BROWSER = os.environ[name_of_browser_var]
        PASSWORD = os.environ[name_of_password_var]
        print BROWSER, PASSWORD
    except KeyError:
        print "Oops! I can not find a variable: " + name_of_browser_var + " or " + name_of_password_var


class ExampleTest(unittest.TestCase):
    USEREMAIL = 'selenium.panichkina'
    USERDOMAIN = '@mail.ru'
    USERNAME = USEREMAIL + USERDOMAIN
    PASSWORD = os.environ['HW4PASSWORD']

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, "CHROME").copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_page()
        auth_form.open_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.top_menu.get_username()
        self.assertEqual(self.USERNAME, user_name)
