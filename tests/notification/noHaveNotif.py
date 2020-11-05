import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.notification import Notification
from tests.login import LoginTest


class NoHaveNotif(unittest.TestCase):
    NO_NOTIFICATION = 'У Вас пока нет уведомлений'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_act = LoginTest()
        login_act.driver = self.driver
        login_act.loginBeforeAllTests()

        notif_page = Notification(self.driver)
        notif_page.open()

        notif_modal = notif_page.notification_modal

        msg = notif_modal.get_msg()

        self.assertEqual(self.NO_NOTIFICATION, msg)
