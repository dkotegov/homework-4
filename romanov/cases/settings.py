import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps as AuthSteps
from romanov.steps.settings import Steps

from romanov.app.driver import connect


class SettingsTest(unittest.TestCase):
    def test_settings_upload_image(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_avatar('/testData/octopus.png')
        settings.find_success_modal()

    def test_settings_upload_large_image(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_avatar('/testData/largeImage.jpg')
        settings.find_info_error()

    def test_settings_change_pass(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_pass()
        settings.find_success_modal()

    def test_settings_change_short_pass(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_pass('123')
        settings.find_info_error()

    def test_settings_change_empty_pass(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_pass('')
        settings.find_info_error()

    def test_settings_change_email(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_email('test123@test123.ru')
        settings.find_success_modal()

    def test_settings_change_empty_email(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_email('')
        settings.find_info_error()

    def test_settings_change_incorrect_email(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_email('test12@@@r.rt')
        settings.find_info_error()

    def test_settings_change_exist_email(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_email('test@test.ru')
        settings.find_info_error()

    def test_settings_change_login(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_login()
        settings.find_success_modal()

    def test_settings_change_short_login(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_login('12')
        settings.find_info_error()

    def test_settings_change_empty_login(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_login('')
        settings.find_info_error()

    def test_settings_change_exist_login(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_login('slava')
        settings.find_info_error()

    def test_settings_change_desc(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_desc('About me')
        settings.find_success_modal()

    def test_settings_refresh_after_change(self):
        settings = Steps()
        AuthSteps.login_app()
        settings.open_settings()
        settings.change_data(email='tes2t@tes2t.ru', desc='test')
        settings.open_settings()
        settings.equal_data(email='tes2t@tes2t.ru', desc='test')