import unittest
from tests.default_setup import default_setup
from tests.pages.restaurant.profile import RestaurantProfilePage
from tests.steps.auth_restaurant import auth_setup


class ChangeRestaurantPhoneFailedTests(unittest.TestCase):
    phone_empty = ""
    phone_busy = "4444444444"
    expected_error_empty = "Номер телефона: Поле должно быть заполнено"
    expected_error_busy = 'Наш сервер говорит "Restaurant with this number already exists"'

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = RestaurantProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_phone_empty(self):
        self.profile_page.set_phone(self.phone_empty)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_phone_error()
        self.assertEqual(error_msg, self.expected_error_empty)

    def test_change_phone_busy(self):
        self.profile_page.set_phone(self.phone_busy)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_main_error()
        self.assertEqual(error_msg, self.expected_error_busy)
