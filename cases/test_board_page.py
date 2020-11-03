import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from pages.login_page import LoginPage


class BoardsPageTest(unittest.TestCase):
    BOARD_NAME = 'TEST BOARD NAME'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')
        self.login_page.sign_in(login, password)

    def tearDown(self):
        self.driver.quit()

    def test_board_create_success(self):
        boards_page = BoardsPage(self.driver)
        boards_page.wait_for_container()
        boards_page.create_board(self.BOARD_NAME)

        board_page = BoardPage(self.driver)
        self.assertEqual(self.BOARD_NAME, board_page.header.get_board_title())

        board_page.header.open_settings()
        board_page.settings_popup.delete_board()
