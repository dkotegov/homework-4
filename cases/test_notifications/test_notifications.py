import os
import unittest

from pages.login_page import LoginPage
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

        self.boards_page = BoardsPage(self.driver)
        self.login_page = LoginPage(self.driver)

        self.login_page.open()
        self.login_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def tearDown(self):
        self.driver.quit()

    def test_toggle_notifications_enable(self):
        self.boards_page.main_header.open_notifications()

        notifications = self.boards_page.notifications

        notifications.toggle_notifications()
        self.assertFalse(notifications.is_notifications_enabled)

        notifications.toggle_notifications()
        self.assertTrue(notifications.is_notifications_enabled)

    def test_toggle_notifications_sound_enable(self):
        self.boards_page.main_header.open_notifications()

        notifications = self.boards_page.notifications

        notifications.toggle_sound()
        self.assertFalse(notifications.is_sound_enabled)

        notifications.toggle_sound()
        self.assertTrue(notifications.is_sound_enabled)

