import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps as AuthSteps
from romanov.steps.profile import Steps

from romanov.app.driver import connect

EMPTY = ""
EMPTY_FEED = "Нет пинов у данного пользователя"
FOLLOW = "Подписаться"
UNFOLLOW = "Отписаться"

class ProfileTest(unittest.TestCase):
    def test_desk_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        link = profile.open_desk()
        self.assertEqual(link, connect.driver.current_url)

    def test_settings_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        link = profile.open_settings()
        self.assertEqual(link, connect.driver.current_url)

    def test_new_pin_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        label = profile.new_pin()
        self.assertNotEqual(label, EMPTY)

    def test_subs_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        link = profile.open_subs()
        self.assertEqual(link, connect.driver.current_url)

    def test_user_pins_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        link = profile.open_user_pins()
        self.assertEqual(link, connect.driver.current_url)

    def test_logout_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile()
        label = profile.logout()
        self.assertNotEqual(label, EMPTY)

    def test_following_zero_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        label = profile.click_empty_followings()
        self.assertEqual(label, EMPTY)

    def test_followers_zero_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        label = profile.click_empty_followers()
        self.assertEqual(label, EMPTY)

    def test_followers_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(2)
        label = profile.click_followers()
        self.assertNotEqual(label, EMPTY)

    def test_following_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(2)
        label = profile.click_followings()
        self.assertNotEqual(label, EMPTY)

    def test_empty_pins_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        label = profile.open_empty_pins()
        self.assertEqual(label, EMPTY_FEED)

    def test_chat_open(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        link = profile.open_chat()
        self.assertEqual(link, connect.driver.current_url)

    def test_following_user(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        label = profile.following()
        self.assertEqual(label, UNFOLLOW)
        label = profile.unfollowing()
        self.assertEqual(label, FOLLOW)

    def test_following_user_refresh(self):
        profile = Steps()
        AuthSteps.login_app(self)
        profile.open_user_profile(50)
        label = profile.following()
        self.assertEqual(label, UNFOLLOW)
        profile.open_user_profile(50)
        label = profile.unfollowing()
        self.assertEqual(label, FOLLOW)