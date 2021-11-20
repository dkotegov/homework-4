import unittest
from tests.default_setup import default_setup
from tests.pages.user.profile import UserProfilePage
from tests.steps.auth_user import auth_setup


class ChangeUserNameFailedTests(unittest.TestCase):
    name_more25 = "arkadiyarkadiyarkadiyarkadiyar"
    name_empty = ""
    expected_error_empty = "Имя: Поле должно быть заполнено"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = UserProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_name_empty(self):
        self.profile_page.set_name(self.name_empty)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_name_error()
        self.assertEqual(error_msg, self.expected_error_empty)
