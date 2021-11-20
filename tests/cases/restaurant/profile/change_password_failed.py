import unittest
from tests.default_setup import default_setup
from tests.pages.restaurant.profile import RestaurantProfilePage
from tests.steps.auth_restaurant import auth_setup


class ChangeRestaurantPasswordFailedTests(unittest.TestCase):
    new_password = "222222"
    password_less6 = "111"
    password_more25 = "arkadiyarkadiyarkadiyarkadiyar"
    different_new_password = "333333"
    wrong_cur_password = "wrong_old"
    expected_error_wrong_old_password = "Текущий пароль: Введен не верный текущий пароль"
    expected_error_different_new_password = "Повторите пароль: Пароли не совпадают"
    expected_error_less_or_more_password = "Новый пароль: Ваш пароль должен быть от 6 до 30 символов"

    def setUp(self):
        default_setup(self)
        self.cur_password = self.RESTAURANT_PASSWORD
        auth_setup(self)
        self.profile_page = RestaurantProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_password_new_less6(self):
        self.profile_page.set_current_password(self.cur_password)
        self.profile_page.set_new_password(self.password_less6)
        self.profile_page.set_repeat_password(self.password_less6)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_new_pass_error()
        self.assertEqual(error_msg, self.expected_error_less_or_more_password)
