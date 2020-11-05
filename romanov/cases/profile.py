import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps as AuthSteps
from romanov.steps.profile import Steps

from romanov.app.driver import connect


class ProfileTest(unittest.TestCase):
    def test_desk_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.open_desk()

    def test_settings_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.open_settings()

    def test_new_pin_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.new_pin()

    def test_subs_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.open_subs()

    def test_user_pins_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.open_user_pins()

    def test_logout_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile()
        profile.logout()

    def test_following_zero_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.click_empty_followings()

    def test_followers_zero_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.click_empty_followers()

    def test_followers_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(2)
        profile.click_followers()

    def test_following_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(2)
        profile.click_followings()

    def test_empty_pins_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.open_empty_pins()

    def test_chat_open(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.open_chat()

    def test_following_user(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.following()
        profile.unfollowing()

    def test_following_user_refresh(self):
        profile = Steps()
        AuthSteps.login_app()
        profile.open_user_profile(50)
        profile.following()
        profile.open_user_profile(50)
        profile.unfollowing()