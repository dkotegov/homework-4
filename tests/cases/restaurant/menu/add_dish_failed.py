import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.pages.restaurant.menu import RestaurantMenuPage
from tests.steps.auth_restaurant import auth_setup
from tests.steps.add_section import add_section_setup
from tests.steps.delete_section import delete_section_setup


class AddDishFailedTest(unittest.TestCase):
    empty = ""
    cost_weight_word = "sfew"
    expected_error_name_empty = "Название блюда: Поле должно быть заполнено"
    expected_error_cost = "Цена: Введите число"
    expected_error_description_empty = "Описание: Поле должно быть заполнено"
    expected_error_weight = "Вес: Введите число"

    def setUp(self):
        self.fake = Faker()
        default_setup(self)
        auth_setup(self)
        self.menu_page = RestaurantMenuPage(self.driver)
        self.menu_page.open()
        self.section_name = add_section_setup(self)

    def tearDown(self):
        self.menu_page.open()
        delete_section_setup(self, self.section_name)
        self.driver.quit()

    def set_default_values(self):
        self.menu_page.set_dish_name(self.fake.first_name())
        self.menu_page.set_dish_description(self.fake.name())
        self.menu_page.set_dish_cost("500")
        self.menu_page.set_dish_weight("200")

    def test_add_dish_name_empty(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_name(self.empty)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_name_error()
        self.assertEqual(error_msg, self.expected_error_name_empty)

    def test_add_dish_cost_empty(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_cost(self.empty)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_cost_error()
        self.assertEqual(error_msg, self.expected_error_cost)

    def test_add_dish_description_empty(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_description(self.empty)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_description_error()
        self.assertEqual(error_msg, self.expected_error_description_empty)

    def test_add_dish_weight_empty(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_weight(self.empty)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_weight_error()
        self.assertEqual(error_msg, self.expected_error_weight)

    def test_add_dish_weight_word(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_weight(self.cost_weight_word)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_weight_error()
        self.assertEqual(error_msg, self.expected_error_weight)

    def test_add_dish_cost_word(self):
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_cost(self.cost_weight_word)
        self.menu_page.save_dish()

        error_msg = self.menu_page.get_dish_cost_error()
        self.assertEqual(error_msg, self.expected_error_cost)
