import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.login import LoginPage
from pages.notification import Notification
from tests.login import LoginTest
from tests.pin_comment_search_menu import PinPage


class HaveNotif(unittest.TestCase):
    COMMENT_TEXT = 'text'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        USERNAME2 = os.environ.get('LOGIN2', 'no_test')
        PASSWORD2 = os.environ.get('PASSWORD2', 'no_test')
        PIN_ID = os.environ.get('PIN_ID', 'no_test')

        if USERNAME2 == 'no_test':
            print('TEST HaveNotif: not have USERNAME2 ! skip')
            return

        if PASSWORD2 == 'no_test':
            print('TEST HaveNotif: not have PASSWORD2 ! skip')
            return

        if PIN_ID == 'no_test':
            print('TEST HaveNotif: not have PIN_ID! skip')
            return

        login_act = LoginTest()
        login_act.driver = self.driver
        login_act.loginBeforeAllTests(second_profile=True)

        pp = PinPage(self.driver)
        pin_path = pp.BASE_URL + 'pin/' + PIN_ID
        pp.open_pin(pin_path)

        comment = pp.pin.comment
        comment.set_comment_text(self.COMMENT_TEXT)
        comment.send_comment()


        lp = LoginPage(self.driver).form
        self.assertTrue(lp.logout())

        self.driver.get(pp.BASE_URL)

        login_act.loginBeforeAllTests()

        notif_page = Notification(self.driver)
        notif_page.open()

        notif_modal = notif_page.notification_modal

        notif_text = notif_modal.get_last_notif_text()

        self.assert_(notif_text, USERNAME2)
        self.assert_(notif_text, self.COMMENT_TEXT)
