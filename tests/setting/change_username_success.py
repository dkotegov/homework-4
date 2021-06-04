import unittest
from tests.default_setup import default_setup
from Pages.settings_page import SettingPage
from Pages.profile_page import ProfilePage
from steps.auth import setup_auth


class UsernameChangeSuccessTests(unittest.TestCase):
    new_login = "abrikos-soska"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.setting_page = SettingPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.setting_page.open()

    def tearDown(self):
        self.setting_page.open()
        self.setting_page.change_username(self.LOGIN)
        self.driver.quit()

    def test_change_password(self):
        self.setting_page.change_username(self.new_login)
        self.setting_page.submit()
        current_login = self.profile_page.get_username()
        self.assertEqual(current_login, self.new_login)
