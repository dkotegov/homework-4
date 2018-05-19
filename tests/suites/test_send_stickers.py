import os

import unittest

from tests.pages.auth import AuthPage
from tests.pages.main import MainPage
from tests.pages.message import MessagePage
from tests.pages.dialog import DialogPage
from tests.pages.dialog_menu import DialogMenuPage
from tests.pages.confirm import ConfirmPage

from selenium.webdriver import DesiredCapabilities, Remote

class TestsSendStickers(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()

        self.BOT_1_LOGIN = "technopark3"
        self.PASSWORD = os.environ['PASSWORD']
        self.CURRENT_DIALOG_URL = ""

        self.dialog_page = DialogPage(self.driver)
        self.message_page = MessagePage(self.driver)
        self.auth_page = AuthPage(self.driver)
        self.auth_page.sign_in(self.BOT_1_LOGIN, self.PASSWORD)
        self.main_page = MainPage(self.driver)
        self.main_page.open_messages()

        self.create_dialog()
        self.CURRENT_DIALOG_URL = self.driver.current_url

    def tearDown(self):
        self.driver.get(self.CURRENT_DIALOG_URL)
        self.delete_dialog()
        self.driver.quit()

    def create_dialog(self):
        self.message_page.create_dialog()
        self.message_page.choose_companion()
        self.dialog_page.wait_for_loader()

    def delete_dialog(self):
        self.dialog_page.open_menu()
        dilog_menu_page = DialogMenuPage(self.driver)
        dilog_menu_page.delete_dialog()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm()

    def test_send_usmile_sticker(self):
        self.dialog_page.send_sticker("USMILE_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_usmile_sticker failed")

    def test_send_usmile_2_sticker(self):
        self.dialog_page.send_sticker("USMILE_STICKER_2")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_usmile_2_sticker failed")

    def test_send_dog_sticker(self):
        self.dialog_page.send_sticker("DOG_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_dog_sticker failed")

    def test_send_fox_sticker(self):
        self.dialog_page.send_sticker("FOX_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_fox_sticker failed")

    def test_send_heart_sticker(self):
        self.dialog_page.send_sticker("HEART_STICKER")
        self.assertTrue(
            self.dialog_page.message_with_sticker_exists(),
            "test_send_heart_sticker failed")