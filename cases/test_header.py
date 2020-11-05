import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.profile_page import ProfilePage


class HeaderTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.boards_page = BoardsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

        self.login_page.open()
        self.login_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def tearDown(self):
        self.driver.quit()

    def test_open_profile(self):
        self.boards_page.open()
        self.boards_page.wait_for_container()
        self.boards_page.main_header.open_profile()

        self.assertTrue(self.profile_page.is_open)

    def test_open_notifications(self):
        self.boards_page.open()
        self.boards_page.wait_for_container()
        self.boards_page.main_header.open_notifications()

        self.assertTrue(self.boards_page.notifications.is_open)

    def test_logout(self):
        self.boards_page.open()
        self.boards_page.wait_for_container()

        self.boards_page.main_header.logout()

        self.assertTrue(self.login_page.is_open)

    def test_open_boards(self):
        self.profile_page.open()
        self.profile_page.wait_for_container()
        self.profile_page.main_header.open_boards()

        self.assertTrue(self.boards_page.is_open)
