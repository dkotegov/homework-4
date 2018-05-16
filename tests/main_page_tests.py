import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.main_page import MainPage


class MainPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        self.driver.quit()
    #
    # def test_open_gifts(self):
    #     gifts_page = self.main_page.open_gifts()
    #     is_loaded = gifts_page.is_loaded()
    #     self.assertTrue(is_loaded)
