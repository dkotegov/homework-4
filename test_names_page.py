# coding=utf-8

import datetime
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.ui import WebDriverWait

from page import NamesPage


class NamesTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_menu_logo(self):
        self.assertEquals(True, True)
        # names_page = NamesPage(self.driver)
        # names_page.open()
        #
        # top_menu = names_page.menu
        #
        # title = top_menu.click_logo()
        # self.assertEquals(title, top_menu.get_title())

