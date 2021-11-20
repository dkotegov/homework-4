import unittest
from faker import Faker
from tests.default_setup import default_setup
from tests.pages.user.profile import UserProfilePage
from tests.steps.auth_user import auth_setup


class ChangeUserDataSuccessTests(unittest.TestCase):
    new_email = "mail@mail.ru"
    new_pass = "123456"

    def setUp(self):
        self.fake = Faker()
        default_setup(self)
        auth_setup(self)
        self.profile_page = UserProfilePage(self.driver)
        self.profile_page.open()
        self.username = self.profile_page.navbar.get_username()

    def tearDown(self):
        self.set_start_data()
        self.driver.quit()

    def set_start_data(self):
        self.profile_page.set_email(self.USER_LOGIN)
        self.profile_page.set_name(self.username)
        self.profile_page.set_current_password(self.new_pass)
        self.profile_page.set_new_password(self.USER_PASSWORD)
        self.profile_page.set_repeat_password(self.USER_PASSWORD)
        self.profile_page.click_save()

    def test_change_all_data(self):
        new_username = self.fake.first_name()
        new_phone = self.fake.phone_number()
        self.profile_page.set_phone(new_phone)
        self.profile_page.set_email(self.new_email)
        self.profile_page.set_name(new_username)
        self.profile_page.set_current_password(self.USER_PASSWORD)
        self.profile_page.set_new_password(self.new_pass)
        self.profile_page.set_repeat_password(self.new_pass)
        self.profile_page.click_save()
        username = self.profile_page.navbar.get_username()
        self.assertEqual(new_username, username)
