import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.gift_page = GiftPage(self.driver)
        self.gift_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_open_authors_gifts(self):
        authors_gift_page = self.gift_page.open_authors_gifts()
        ok = authors_gift_page.is_loaded()
        self.assertTrue(ok)

    def test_open_actual_gifts(self):
        # opening actual gifts page
        # actual_gift_page = self.gift_page.open_actual_gifts()
        # ok = actual_gift_page.is_loaded()

        # opening authors gifts page
        # authors_gift_page = self.gift_page.open_authors_gifts()

        #trying to open actual gifts page second time
        actual_gift_page = self.gift_page.open_actual_gifts()
        ok = actual_gift_page.is_loaded()
        self.assertTrue(ok)

    def test_open_postcards(self):
        postcards_page = self.gift_page.open_postcards()
        ok = postcards_page.is_loaded()
        self.assertTrue(ok)

    def test_open_vip_gifts(self):
        vip_gift_page = self.gift_page.open_vip_gifts()
        ok = vip_gift_page.is_loaded()
        self.assertTrue(ok)

    def test_create_gift(self):
        create_gift_page = self.gift_page.open_create_gift()
        ok = create_gift_page.is_loaded()
        self.assertTrue(ok)

    def test_send_gift_secretly(self):
        gift_page = self.gift_page.send_gift_secretly()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    def test_send_gift_private(self):
        gift_page = self.gift_page.send_gift_private()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    def test_send_gift_usual(self):
        gift_page = self.gift_page.send_gift_usual()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    def test_search_gift(self):
        search_gift_page = self.gift_page.search_gift()
        ok = search_gift_page.is_search_done()
        self.assertTrue(ok)

    def test_send_gift_by_receivers_name(self):
        gift_page = self.gift_page.send_gift_by_receivers_name()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)
