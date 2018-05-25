import os

import unittest

from tests.pages.auth import AuthPage
from tests.pages.main import MainPage
from tests.pages.message import MessagePage
from tests.pages.dialog import DialogPage
from tests.pages.dialog_menu import DialogMenuPage
from tests.pages.confirm import ConfirmPage

from selenium.webdriver import DesiredCapabilities, Remote


class TestsSendDocuments(unittest.TestCase):

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

    def test_send_document_txt(self):
        self.dialog_page.send_document(os.getcwd() + "/tests/static/awd.txt")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_document_txt failed")

    def test_send_document_video(self):
        self.dialog_page.send_document(
            os.getcwd() + "/tests/static/sabaton_low.mp4")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_document_video failed")

    def test_send_document_photo(self):
        self.dialog_page.send_document(
            os.getcwd() + "/tests/static/sabaton_low.jpeg")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_document_photo failed")

    def test_send_document_pages(self):
        self.dialog_page.send_document(
            os.getcwd() + "/tests/static/sabaton.pages")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_document_pages failed")

    def test_send_photo(self):
        self.dialog_page.send_photo(os.getcwd() + "/tests/static/sabaton.jpg")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_photo failed")

    def test_send_photo_wrong_format(self):
        self.dialog_page.send_photo(os.getcwd() + "/tests/static/awd.txt")
        self.assertTrue(
            self.dialog_page.get_wrong_photo_format(),
            "test_send_photo_wrong_format failed")

    def test_send_photo_high_res(self):
        self.dialog_page.send_photo(
            os.getcwd() + "/tests/static/sabaton_high.jpg")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_photo_high_res failed")

    def test_send_photo_low_res(self):
        self.dialog_page.send_photo(
            os.getcwd() + "/tests/static/sabaton_low.jpeg")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_photo_low_res failed")

    def test_send_photo_png_format(self):
        self.dialog_page.send_photo(
            os.getcwd() + "/tests/static/sabaton_png.png")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_photo_png_format failed")

    def test_send_video_low_res(self):
        self.dialog_page.send_video(
            os.getcwd() + "/tests/static/sabaton_low.mp4")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_video_low_res failed")

    def test_send_video_high_res(self):
        self.dialog_page.send_video(
            os.getcwd() + "/tests/static/sabaton_high.mp4")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_video_high_res failed")

    def test_send_video_no_sound(self):
        self.dialog_page.send_video(
            os.getcwd() + "/tests/static/sabaton_no_sound.mp4")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_video_no_sound failed")

    def test_send_video_webm_fromat(self):
        self.dialog_page.send_video(
            os.getcwd() + "/tests/static/sabaton_webm.webm")
        self.assertTrue(
            self.dialog_page.sent_message_exists(),
            "test_send_video_webm_fromat failed")

    def test_send_video_wrong_fromat(self):
        self.dialog_page.send_video(os.getcwd() + "/tests/static/awd.txt")
        self.assertTrue(
            self.dialog_page.get_wrong_photo_format(),
            "test_send_video_webm_fromat failed")
