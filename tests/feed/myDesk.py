import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.feed import FeedPage
from pages.notification import Notification
from pages.profile import ProfilePage
from tests.login import LoginTest
from tests.pin_comment_search_menu import PinPage


class MyDesk(unittest.TestCase):
    INFOMESSAGE = 'Ок'

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

        self.driver.refresh()

        pp = PinPage(self.driver)
        pp.open_pin()
        pin = pp.pin
        pin.click_on_save_pin()
        pinId = pin.save_pin()

        self.assertEqual(pin.get_save_info(), self.INFOMESSAGE)

        self.driver.refresh()

        notif_page = Notification(self.driver)
        top_menu = notif_page.top_menu
        top_menu.go_to_my_profile()

        profile_page = ProfilePage(self.driver)
        profile_area = profile_page.profile_area
        profile_area.click_my_desk()

        feed_page = FeedPage(self.driver)
        feed_area = feed_page.feed_area

        ids = feed_area.get_pins_id()

        isContainsId = False

        for i in ids:
            if i == pinId:
                isContainsId = True

        self.assertTrue(isContainsId)

