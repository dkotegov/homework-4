import unittest
from tests.default_setup import default_setup
from tests.pages.restaurant.profile import RestaurantProfilePage
from tests.steps.auth_restaurant import auth_setup


class ChangeRestaurantCostFailedTests(unittest.TestCase):
    cost_more25 = "38472983982375674297423782343"
    cost_word = "sdkfjdl"
    cost_empty = ""
    expected_error_more = "Стоимость доставки: Поле должно содержать меньше 25 символов"
    expected_error_empty = "Стоимость доставки: Поле должно быть заполнено"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = RestaurantProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_cost_more25(self):
        self.profile_page.set_cost(self.cost_more25)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_cost_error()
        self.assertEqual(error_msg, self.expected_error_more)

    def test_change_cost_empty(self):
        self.profile_page.set_cost(self.cost_empty)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_cost_error()
        self.assertEqual(error_msg, self.expected_error_empty)

    def test_change_cost_word(self):
        self.profile_page.set_cost(self.cost_word)
        self.profile_page.click_save()
        error_msg = self.profile_page.get_cost_error()
        self.assertEqual(error_msg, self.expected_error_empty)
