import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from pages.notification import Notification


class NoLoginNotif(unittest.TestCase):

    LOAD_MSG = 'Ошибка обработки запроса'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        notif_page = Notification(self.driver)
        notif_page.open()

        notif_modal = notif_page.notification_modal

        msg = notif_modal.get_load_notif_msg()

        self.assertEqual(self.LOAD_MSG, msg)
