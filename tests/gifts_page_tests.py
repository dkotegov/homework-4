import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage
from src.pages.main_page import MainPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.gift_page = GiftPage(self.driver)
        self.gift_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_open_main_page(self):
        main_page = self.gift_page.open_main_page()
        ok = main_page.is_loaded()
        print(ok)
        self.assertTrue(ok)



