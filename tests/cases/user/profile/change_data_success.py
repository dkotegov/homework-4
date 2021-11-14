import unittest
from tests.default_setup import default_setup
from tests.pages.user.profile import ProfilePage
from tests.steps.auth_user import auth_setup


class ChangeDataSuccessTests(unittest.TestCase):
    new_phone = "9197666701"
    new_email = "mail@mail.ru"
    new_name = "Олег"
    new_pass = "123456"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.set_start_data()
        self.driver.quit()

    def set_start_data(self):
        self.profile_page.set_email(self.USER_LOGIN)
        self.profile_page.set_current_password(self.new_pass)
        self.profile_page.set_new_password(self.USER_PASSWORD)
        self.profile_page.set_repeat_password(self.USER_PASSWORD)
        self.profile_page.click_save()

    def test_change_all_data(self):
        self.profile_page.set_phone(self.new_phone)
        self.profile_page.set_email(self.new_email)
        self.profile_page.set_name(self.new_name)
        self.profile_page.set_current_password(self.USER_PASSWORD)
        self.profile_page.set_new_password(self.new_pass)
        self.profile_page.set_repeat_password(self.new_pass)
        self.profile_page.click_save()
        username = self.auth_page.navbar.get_username()
        self.assertEqual(self.new_name, username)
