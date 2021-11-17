import unittest
from tests.default_setup import default_setup
from tests.pages.user.profile import UserProfilePage
from tests.steps.auth_user import auth_setup


class ChangeUserEmailFailedTests(unittest.TestCase):
    email_more25 = "arkadiyarkadiyarkadiya@mail.ru"
    email_empty = ""
    email_incorrect = "oleg"
    expected_error_more = "Почта: Поле должно содержать меньше 25 символов"
    expected_error_empty = "Почта: Поле должно быть заполнено"
    expected_error_incorrect = "Почта: Введите настоящий адрес электронной почты"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = UserProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.set_start_email()
        self.driver.quit()

    def set_start_email(self):
        self.profile_page.set_email(self.USER_LOGIN)
        self.profile_page.click_save()

    def test_change_email_more25(self):
        self.profile_page.set_email(self.email_more25)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_email_error()
        self.assertEqual(error_msg, self.expected_error_more)

    def test_change_email_empty(self):
        self.profile_page.set_email(self.email_empty)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_email_error()
        self.assertEqual(error_msg, self.expected_error_empty)

    def test_change_email_incorrect(self):
        self.profile_page.set_email(self.email_incorrect)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_email_error()
        self.assertEqual(error_msg, self.expected_error_incorrect)
