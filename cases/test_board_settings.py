import os
import unittest
import time

from pages.login_page import LoginPage
from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class HeaderTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.board_page = BoardPage(self.driver)
        self.boards_page = BoardsPage(self.driver)

        self.login_page.open()
        self.login_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

        self.BOARD_NAME = 'Очередная доска ' + str(time.time())
        self.boards_page.open()
        self.boards_page.create_board(self.BOARD_NAME)
        self.board_page.header.open_settings()

    def tearDown(self):
        self.driver.quit()

    def test_change_board_name(self):
        new_board_name = 'Новая досочка'
        settings = self.board_page.settings_popup

        settings.change_name(new_board_name)
        settings.wait_for_container()

        settings.close_popup()
        self.board_page.wait_for_container()

        self.assertTrue(self.board_page.header.check_title(new_board_name))

        self.board_page.header.open_settings()
        settings.delete_board()

    def test_generate_invite_link(self):
        settings = self.board_page.settings_popup

        old_link = settings.get_link_text()
        settings.generate_link()
        settings.wait_for_container()
        new_link = settings.get_link_text()

        self.assertNotEqual(old_link, new_link)

        settings.delete_board()

    def test_delete_board(self):
        self.board_page.settings_popup.delete_board()
        self.assertTrue(self.boards_page.is_open)

    def test_invite_member(self):
        settings = self.board_page.settings_popup
        invitee_nickname = 'asdasd'

        settings.invite_member(invitee_nickname)
        settings.wait_for_container()
        settings.wait_for_container()
        settings.wait_for_container()
        settings.wait_for_container()  # как-то так(((

        self.assertEqual(settings.get_members_count(), 2)

        settings.delete_board()

    def test_open_member_nickname(self):
        settings = self.board_page.settings_popup
        settings.open_member(0)

        nickname = settings.get_member_nickname(0)
        self.assertEqual(os.environ.get('LOGIN'), nickname)

        settings.delete_board()
