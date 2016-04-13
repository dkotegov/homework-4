# -*- coding: utf-8 -*-
import os

from selenium.webdriver import Remote, DesiredCapabilities, ActionChains

from pages.pages import ActorProfilePage
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class MainHeaderTestCase(BaseTestCase):
    def test_main_header(self):
        self.page = ActorProfilePage(self.driver)
        self.page.open()
        self.assertEqual(1, 1)
