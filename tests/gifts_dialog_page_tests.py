import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage
from src.pages.self_gift_page import SelfGiftPage
from src.pages.gift_dialog_page import GiftDialogPage


class GiftDialogPageTests(unittest.TestCase):

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

        self.gift_page.open_self_gifts()
        if not self.gift_page.check_gift_exist():
            self.gift_page.create_new_gift()
        else:
            self.self_gift.open_gift_dialog()
            while self.gift_dialog_page.comment_is_exist():
                self.delete_comment()

        self.gift_page.open_without_auth()

    def tearDown(self):
        self.driver.quit()


    #grigorevpv
    def open_self_gifts(self):
        self.gift_page.open_self_gifts()

    def create_text_comment(self, text):
        self.gift_dialog_page.send_text_comment(text)

    def delete_comment(self):
        self.gift_dialog_page.delete_comment()

    def read_file(self, fname):
        with open(fname, 'r') as f:
            try:
                text = f.read()
                return text
            except:
                print "Could not read file:", fname

    # def test_set_like_gift(self):
    #     self.open_self_gifts()
    #     self.self_gift.like_gift()
    #     self.assertTrue(self.gift_page.like_gift_exists(), "test_send_sticker failed")

    def test_send_sticker(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_sticker()
        self.assertTrue(self.gift_dialog_page.comment_with_sticker_exists(), "test_send_sticker failed")

    def test_send_photo(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_photo()
        self.assertTrue(self.gift_dialog_page.comment_with_photo_exists(), "test_send_photo failed")

    def test_send_video(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_video()
        self.assertTrue(self.gift_dialog_page.comment_with_video_exists(), "test_send_video failed")

    def send_jpeg_photo(self):
        # send gif image
        self.gift_dialog_page.send_photo_from_computer("/staticfiles/jpeg_image.jpeg")
        self.assertTrue(self.gift_dialog_page.comment_with_photo_from_computer_exists(),
                        "test_send_jpeg_photo_from_computer failed")

    def send_gif_photo(self):
        # send gif image
        self.gift_dialog_page.send_photo_from_computer("/staticfiles/gif_image.gif")
        self.assertTrue(self.gift_dialog_page.comment_with_photo_from_computer_exists(),
                        "test_send_gif_photo_from_computer failed")

    def test_send_png_photo(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        # send png image
        self.gift_dialog_page.send_photo_from_computer("/staticfiles/png_image.png")
        self.assertTrue(self.gift_dialog_page.comment_with_photo_from_computer_exists(),
                        "test_send_png_photo_from_computer failed")

    def test_send_photo_from_computer(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.send_gif_photo()
        # self.send_png_photo()
        self.send_jpeg_photo()

    def test_set_friend(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_friend()
        self.assertTrue(self.gift_dialog_page.comment_with_user_exists(), "test_set_friend failed")

    def test_send_text_comment(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        # send simple text message
        self.create_text_comment("Test text message")
        self.assertTrue(self.gift_dialog_page.comment_with_text_exists(), "test_send_simple_text_comment failed")
        self.delete_comment()
        # send empty text message
        self.create_text_comment("")
        self.assertFalse(self.gift_dialog_page.comment_with_text_exists(), "test_send_empty_text_comment failed")
        # send big text message
        text = self.read_file('./staticfiles/text_message.txt')
        self.create_text_comment(text)
        self.assertTrue(self.gift_dialog_page.comment_with_text_exists(), "test_send_big_text_comment failed")

    def test_delete_comment(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.create_text_comment("Test delete comment!")
        self.delete_comment()
        self.assertFalse(self.gift_dialog_page.comment_with_delete_text_exists(), "test_delete_comment failed")

    def test_change_text_comment(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.create_text_comment("Test comment!")
        self.gift_dialog_page.change_text_comment("Changed text!")
        self.assertTrue(self.gift_dialog_page.comment_with_change_text_exists(), "test_change_text_comment failed")

    def test_like_comment(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.create_text_comment("Like comment!")
        self.gift_dialog_page.like_comment()
        self.assertTrue(self.gift_dialog_page.like_comment_exists(), "test_like_comment failed")
