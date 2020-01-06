# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.SettingsPage import SettingsPage


class SettingsTest(BasicTest):
    SETTINGS_OK_URL = 'https://e.mail.ru/settings?result=ok&afterReload=1'
    SETTINGS_NOTIFICATIONS_URL = 'https://e.mail.ru/settings/notifications'

    def pre_tests(self):
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.open()
        self.auth()
        self.settings_page.wait_redirect(self.settings_page.SETTINGS_URL)

    def test_save(self):
        self.settings_page.enter_firstname('New name')
        self.settings_page.save()
        self.settings_page.wait_redirect(self.SETTINGS_URL)
        self.assertEqual(self.driver.current_url, self.SETTINGS_OK_URL)

    def test_save_empty_field(self):
        self.settings_page.enter_firstname('')
        self.settings_page.save()
        self.settings_page.wait_render(self.settings_page.error_field_message)
        self.settings_page.wait_render(self.settings_page.error_message)

    def test_edit_city(self):
        city = 'Москва'
        self.settings_page.enter_city(city.decode('utf-8'))
        self.settings_page.choose_city()
        self.settings_page.save()
        self.settings_page.wait_redirect(self.SETTINGS_URL)
        self.assertEqual(self.driver.current_url, self.SETTINGS_OK_URL)

    def test_switch_notifications(self):
        self.settings_page.notification_settings()
        self.settings_page.wait_redirect(self.SETTINGS_NOTIFICATIONS_URL)
        self.settings_page.notification_change_mode()
        self.settings_page.wait_render(self.settings_page.save_message)
