# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from src.auth_factory import AuthFactory
from src.pages.auth_page import AuthPage


class Tests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self._auth = AuthFactory.create(username='technopark8')

        self.auth_page = AuthPage(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_open(self):
        self.auth_page.open()
        self.auth_page.sign_in(self._auth.username, self._auth.password)
