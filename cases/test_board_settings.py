import os
import unittest

from pages.login_page import LoginPage
from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException


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

        self.BOARD_NAME = 'Очередная доска'
        self.boards_page.open()
        self.boards_page.create_board(self.BOARD_NAME)
        self.board_page.header.open_settings()

    def tearDown(self):
        try:
            self.board_page.header.open_settings()
        except StaleElementReferenceException:
            pass
        except ElementClickInterceptedException:
            pass
        finally:
            self.board_page.settings_popup.delete_board()
            self.driver.quit()

    def test_change_board_name(self):
        new_board_name = 'Новая досочка'
        settings = self.board_page.settings_popup

        settings.change_name(new_board_name)
        settings.wait_for_visible()

        settings.close_popup()
        self.board_page.wait_for_container()

        self.assertTrue(self.board_page.header.check_title(new_board_name))

    def test_generate_invite_link(self):
        settings = self.board_page.settings_popup

        old_link = settings.get_link_text()
        settings.generate_link()
        settings.wait_for_visible()
        new_link = settings.get_link_text()

        self.assertNotEqual(old_link, new_link)



    # def test_delete_board(self):
    #     pass
    #
    # def test_invite_member(self):
    #     pass
    #
    # def test_open_member_nickname(self):
    #     pass
