import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.notification import Notification
from tests.login import LoginTest


class HaveNotif(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        USERNAME = os.environ.get('LOGIN2', 'no_test')
        PASSWORD = os.environ.get('PASSWORD2', 'no_test')

        if USERNAME == PASSWORD == 'no_test':
            print('TEST HaveNotif: not have LOGIN2 and PASSWORD2! skip')
            return

        login_act = LoginTest()
        login_act.driver = self.driver
        login_act.loginBeforeAllTests(second_profile=True)

        # write comment

        self.driver.delete_all_cookies()
        self.driver.refresh()

        login_act.loginBeforeAllTests()

        notif_page = Notification(self.driver)
        notif_page.open()

        notif_modal = notif_page.notification_modal

        #get some notif

        #msg = notif_modal.get_msg()
        #self.assertEqual(self.NO_NOTIFICATION, msg)
