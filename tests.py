# -*- coding: utf-8 -*-

import os

import unittest
import urlparse
import Pages

from selenium import webdriver

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait


class TestPlan(unittest.TestCase):
    # LOGIN = os.environ['LOGIN']
    # PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        print browser

        self.driver = webdriver.Chrome("/Users/robert/Documents/ТЕСТИРОВКА/chromedriver")

        # self.driver = Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        # )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_page = Pages.LoginPage(self.driver)
        login_page.open()
        main_page = login_page.login("bikemaster2000@list.ru.local", "park3791")
        post_page = main_page.get_post()
        content_size = post_page.check_last_comment()
        self.assertNotEqual(content_size, 0)
