import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage
from src.pages.self_gift_page import SelfGiftPage
from src.pages.gift_dialog_page import GiftDialogPage


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.gift_page = GiftPage(self.driver)
        self.self_gift = SelfGiftPage(self.driver)
        self.gift_dialog_page = GiftDialogPage(self.driver)
        self.gift_page.open()

    def tearDown(self):
        self.driver.quit()

    #pitikdmitry

    # def test_open_authors_gifts(self):
    #     authors_gift_page = self.gift_page.open_authors_gifts()
    #     ok = authors_gift_page.is_loaded()
    #     self.assertTrue(ok)

    # def test_open_actual_gifts(self):
    #     # opening actual gifts page
    #     # actual_gift_page = self.gift_page.open_actual_gifts()
    #     # ok = actual_gift_page.is_loaded()
    #
    #     # opening authors gifts page
    #     # authors_gift_page = self.gift_page.open_authors_gifts()
    #
    #     #trying to open actual gifts page second time
    #     actual_gift_page = self.gift_page.open_actual_gifts()
    #     ok = actual_gift_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_postcards(self):
    #     postcards_page = self.gift_page.open_postcards()
    #     ok = postcards_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_vip_gifts(self):
    #     vip_gift_page = self.gift_page.open_vip_gifts()
    #     ok = vip_gift_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_create_gift(self):
    #     create_gift_page = self.gift_page.open_create_gift()
    #     ok = create_gift_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_send_gift_secretly(self):
    #     gift_page = self.gift_page.send_gift_secretly()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)
    #
    # def test_send_gift_private(self):
    #     gift_page = self.gift_page.send_gift_private()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)
    #
    # def test_send_gift_usual(self):
    #     gift_page = self.gift_page.send_gift_usual()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)
    #
    # def test_search_gift(self):
    #     search_gift_page = self.gift_page.search_gift()
    #     ok = search_gift_page.is_search_done()
    #     self.assertTrue(ok)
    #
    # def test_send_gift_by_receivers_name(self):
    #     gift_page = self.gift_page.send_gift_by_receivers_name()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)


    #grigorevpv

    def open_self_gifts(self):
        self.gift_page.open_self_gifts()

    def create_text_comment(self, text):
        self.gift_dialog_page.send_text_comment(text)

    def delete_comment(self):
        self.gift_dialog_page.delete_comment()

    # def test_set_like_gift(self):
    #     self.open_self_gifts()
    #     self.self_gift.like_gift()
    #     self.assertTrue(self.gift_page.like_gift_exists(), "test_send_sticker failed")

    def test_send_sticker(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_sticker()
        self.assertTrue(self.gift_dialog_page.comment_with_sticker_exists(), "test_send_sticker failed")
        self.delete_comment()
