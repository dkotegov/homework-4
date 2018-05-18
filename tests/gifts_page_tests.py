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
    #
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
    #
    # def test_set_like_gift(self):
    #     self.open_self_gifts()
    #     self.self_gift.like_gift()
    #     self.assertTrue(self.gift_page.like_gift_exists(), "test_send_sticker failed")
    #
    # def test_send_sticker(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.gift_dialog_page.send_sticker()
    #     self.assertTrue(self.gift_dialog_page.comment_with_sticker_exists(), "test_send_sticker failed")
    #     self.delete_comment()

    def test_send_photo(self):
        self.open_self_gifts()
        self.self_gift.open_gift_dialog()
        self.gift_dialog_page.send_photo()
        self.assertTrue(self.gift_dialog_page.comment_with_photo_exists(), "test_send_photo failed")
        self.delete_comment()

    # def test_send_video(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.gift_dialog_page.send_video()
    #     self.assertTrue(self.gift_dialog_page.comment_with_video_exists(), "test_send_video failed")
    #     self.delete_comment()
    #
    # def test_send_photo_from_computer(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.gift_dialog_page.send_photo_from_computer()
    #     self.assertTrue(self.gift_dialog_page.comment_with_photo_from_computer_exists(), "test_send_photo_from_computer failed")
    #     self.delete_comment()
    #
    # def test_set_friend(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.gift_dialog_page.send_friend()
    #     self.assertTrue(self.gift_dialog_page.comment_with_user_exists(), "test_send_photo_from_computer failed")
    #     self.delete_comment()
    #
    # def test_send_text_comment(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.create_text_comment("Hello!")
    #     self.assertTrue(self.gift_dialog_page.comment_with_text_exists(), "test_send_text_comment failed")
    #     self.delete_comment()
    #
    # def test_delete_comment(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.create_text_comment("Test delete comment!")
    #     # self.gift_dialog_page.delete_comment()
    #     self.delete_comment()
    #     self.assertFalse(self.gift_dialog_page.comment_with_delete_text_exists(), "test_delete_comment failed")
    #
    # def test_change_text_comment(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.create_text_comment("Test comment!")
    #     self.gift_dialog_page.change_text_comment("Changed text!")
    #     self.assertTrue(self.gift_dialog_page.comment_with_change_text_exists(), "test_change_text_comment failed")
    #     self.delete_comment()
    #
    # def test_like_comment(self):
    #     self.open_self_gifts()
    #     self.self_gift.open_gift_dialog()
    #     self.create_text_comment("Like comment!")
    #     self.gift_dialog_page.like_comment()
    #     self.assertTrue(self.gift_dialog_page.like_comment_exists(), "test_like_comment failed")
    #     self.delete_comment()

    # ZubAnt
    # def test_open_feed_page_by_logo(self):
    #     feed_page = self.gift_page.open_feed_page_by_logo()
    #     ok = feed_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_feed_page_by_nav_menu(self):
    #     feed_page = self.gift_page.open_feed_page_by_nav_menu()
    #     ok = feed_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_friends_page_by_nav_menu(self):
    #     friends_page = self.gift_page.open_friends_page_by_nav_menu()
    #     ok = friends_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_photo_page_by_nav_menu(self):
    #     photo_page = self.gift_page.open_photo_page_by_nav_menu()
    #     ok = photo_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_groups_page_by_nav_menu(self):
    #     groups_page = self.gift_page.open_groups_page_by_nav_menu()
    #     ok = groups_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_games_page_by_nav_menu(self):
    #     games_page = self.gift_page.open_games_page_by_nav_menu()
    #     ok = games_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_notes_page_by_nav_menu(self):
    #     notes_page = self.gift_page.open_notes_page_by_nav_menu()
    #     ok = notes_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_inventories_page_by_nav_menu(self):
    #     inventories_page = self.gift_page.open_inventories_page_by_nav_menu()
    #     ok = inventories_page.is_loaded()
    #     self.assertTrue(ok)
    #
    # def test_open_own_gifts_page_by_nav_menu(self):
    #     own_gifts_page = self.gift_page.open_own_gifts()
    #     ok = own_gifts_page.is_loaded()
    #     self.assertTrue(ok)
    #
    #     ok = own_gifts_page.is_loaded_own_gifts()
    #     self.assertTrue(ok)
    #
    # def test_add_music(self):
    #     music_editor = self.gift_page.open_add_music_editor()
    #     gift_page = music_editor.select_sound()
    #     ok = gift_page.is_added_music()
    #     self.assertTrue(ok)
    #
    # def test_send_usual_gift_with_music(self):
    #     self.gift_page.add_music()
    #     gift_page = self.gift_page.send_gift_usual()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)
    #
    # def test_send_private_gift_with_music(self):
    #     self.gift_page.add_music()
    #     gift_page = self.gift_page.send_gift_private()
    #     ok = gift_page.is_gift_sent()
    #     self.assertTrue(ok)
