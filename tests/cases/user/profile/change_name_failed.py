import unittest
from tests.default_setup import default_setup
from tests.pages.user.profile import ProfilePage
from tests.steps.auth_user import auth_setup


class ChangeNameFailedTests(unittest.TestCase):
    name_more25 = "arkadiyarkadiyarkadiyarkadiyar"
    name_empty = ""
    expected_error_more = "Имя: Поле должно содержать меньше 25 символов"
    expected_error_empty = "Имя: Поле должно быть заполнено"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_name_more25(self):
        self.profile_page.set_name(self.name_more25)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_name_error()
        self.assertEqual(error_msg, self.expected_error_more)

    def test_change_name_empty(self):
        self.profile_page.set_name(self.name_empty)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_name_error()
        self.assertEqual(error_msg, self.expected_error_empty)
