import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage
from pages.boards_page import BoardsPage


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

        self.login_page.open()
        self.login_page.sign_in(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def test_toggle_notifications_enable(self):
        self.boards_page.main_header.open_notifications()
        notifications = self.boards_page.notifications
        notifications.toggle_notifications()
        self.assertTrue(notifications.is_notifications_enabled())
        notifications.toggle_notifications()
        self.assertFalse(notifications.is_notifications_enabled())
    #
    # def test_toggle_notifications_sound_enable(self):
    #     pass
    #
    # def test_read_notifications(self):
    #     pass
    #
    # def test_delete_notifications(self):
    #     pass
    #
    # def test_notification_link(self):
    #     pass
