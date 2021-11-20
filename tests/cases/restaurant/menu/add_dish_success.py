import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.pages.restaurant.menu import RestaurantMenuPage
from tests.steps.auth_restaurant import auth_setup
from tests.steps.add_section import add_section_setup
from tests.steps.delete_section import delete_section_setup


class AddDishSuccessTest(unittest.TestCase):

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

    def test_add_dish(self):
        dish_name = self.fake.first_name()
        self.menu_page.open_new_dish_form_in_section(self.section_name)
        self.set_default_values()
        self.menu_page.set_dish_name(dish_name)
        self.menu_page.save_dish()
        self.menu_page.wait_until_dish_load(dish_name)

        dishes_name = self.menu_page.get_all_dishes_name()
        self.assertIn(dish_name, dishes_name)
