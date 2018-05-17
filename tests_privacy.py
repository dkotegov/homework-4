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

    def test_my_age_only_friends(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()

        initial_checked_radiobutton = privacy_page.my_age_only_friends()
        initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")

        if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
            privacy_page.click(privacy_page.my_age_all_users())
            privacy_page.click(privacy_page.my_age_only_friends())
        else:
            privacy_page.click(privacy_page.my_age_only_friends())
       
        privacy_page.click(privacy_page.save())


        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK43)
        user_test_page.open()
        user_test_page.add_to_friend()

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        user_test_page.accept_friend()
        checked_age = user_test_page.age()
        self.assertEqual(age, checked_age)

        user_test_page.del_friend()

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        checked_age = user_test_page.age()
        self.assertNotEqual(age, checked_age)

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        initial_checked_radiobutton = privacy_page.my_age_by_value(initial_checked_radiobutton_value)
        if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
            privacy_page.click(initial_checked_radiobutton)
            privacy_page.click(privacy_page.save())



    def test_my_age_all_users(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        age = user_test_page.age()

        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()

        initial_checked_radiobutton = privacy_page.my_age_all_users()
        initial_checked_radiobutton_value = initial_checked_radiobutton.get_attribute("value")
        print(initial_checked_radiobutton_value)
        if(privacy_page.is_cheked_element(initial_checked_radiobutton)):
            privacy_page.click(privacy_page.my_age_only_friends())
            privacy_page.click(privacy_page.my_age_all_users())
        else:
            privacy_page.click(privacy_page.my_age_all_users())
       
        privacy_page.click(privacy_page.save())

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        user_test_page = UserPage(self.driver, profiles.PROFILE_URL_TECHNOPARK42)
        user_test_page.open()
        if user_test_page.is_friend() == True:
            user_test_page.del_friend()

        checked_age = user_test_page.age()
        self.assertEqual(age, checked_age)

        auth_page.logout()
        auth_page.add_profile(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)
        privacy_page = PrivacyPage(self.driver)
        privacy_page.open()
        initial_checked_radiobutton = privacy_page.my_age_by_value(initial_checked_radiobutton_value)
        if(not privacy_page.is_cheked_element(initial_checked_radiobutton)):
            privacy_page.click(initial_checked_radiobutton)
            privacy_page.click(privacy_page.save())
