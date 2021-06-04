import os

import unittest
from tests.default_setup import default_setup
from Pages.settings_page import SettingPage
from steps.auth import setup_auth
from steps.logout import logout

class PasswordSuccessTests(unittest.TestCase):
    old_password = os.environ['PASSWORD']
    new_password = "Arkady123"
    notification_success = "Данные сохранены"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.setting_page = SettingPage(self.driver)
        self.setting_page.open()

    def tearDown(self):
        self.setting_page.open()
        self.setting_page.change_password(self.new_password, self.old_password, self.old_password)
        self.driver.quit()

    def test_change_password(self):
        self.setting_page.set_old_pass(self.old_password)
        self.setting_page.set_new_pass(self.new_password)
        self.setting_page.set_new_pass_confirm(self.new_password)
        self.setting_page.submit()
        notification_text = self.setting_page.get_notification_text()
        self.assertEqual(notification_text, self.notification_success)