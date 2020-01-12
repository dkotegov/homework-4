# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.SettingsPage import SettingsPage
from pages.LoginPage import LoginPage


class SettingsTest(BasicTest):
    AUTH_URL = 'https://e.mail.ru/login'
    SETTINGS_URL = 'https://e.mail.ru/settings'
    SETTINGS_OK_URL = 'https://e.mail.ru/settings?result=ok&afterReload=1'
    SETTINGS_MESSAGES_URL = 'https://e.mail.ru/settings/messages'

    def setUp(self):
        super(SettingsTest, self).setUp()
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.open()
        self.auth()
        self.settings_page.wait_redirect(self.SETTINGS_URL)

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.wait_redirect(self.AUTH_URL)
        login_page.open_iframe(login_page.auth_frame)
        login_page.sign_in(self.login, self.password)

    def test_save(self):
        self.settings_page.enter_firstname('New name')
        self.settings_page.save()
        self.settings_page.wait_redirect(self.SETTINGS_URL)
        self.assertEqual(self.driver.current_url, self.SETTINGS_OK_URL)

    def test_save_fields(self):
        self.settings_page.enter_firstname('Another new name')
        self.settings_page.enter_lastname('New last name')
        self.settings_page.enter_nickname('New nick name')
        self.settings_page.save()
        self.settings_page.wait_redirect(self.SETTINGS_URL)
        self.assertEqual(self.driver.current_url, self.SETTINGS_OK_URL)

    def test_save_empty_field(self):
        self.settings_page.enter_firstname('')
        self.settings_page.save()
        self.settings_page.wait_render(self.settings_page.error_field_message)
        self.settings_page.wait_render(self.settings_page.error_message)

    def test_switch_mailling(self):
        self.settings_page.mailling_settings()
        self.settings_page.wait_redirect(self.SETTINGS_MESSAGES_URL)
        self.settings_page.mailling_switch()
        self.settings_page.save_mailling()
        self.assertEqual(self.driver.current_url, self.SETTINGS_OK_URL)
