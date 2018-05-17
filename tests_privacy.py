import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from pages.auth_page import AuthPage
from pages.privacy_page import PrivacyPage
from pages.friends_page import FriendsPage
from pages.main_page import MainPage
from pages.user_page import UserPage


class TestsPrivacy(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_tag_me_in_photo_only_friends(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()

        initial_checked_radiobutton = privacy_page.tag_my_in_photo_only_friends()

        if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
            privacy_page.click(privacy_page.tag_my_in_photo_no_one())
            privacy_page.click(privacy_page.tag_my_in_photo_only_friends())
        else:
            privacy_page.click(privacy_page.tag_my_in_photo_only_friends())
       
        privacy_page.click(privacy_page.save())


        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.accept_friend()



        time.sleep(5)

