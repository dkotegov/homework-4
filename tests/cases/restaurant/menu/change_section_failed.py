import unittest

from tests.default_setup import default_setup
from tests.pages.restaurant.menu import RestaurantMenuPage
from tests.steps.auth_restaurant import auth_setup


class ChangeSectionFailedTest(unittest.TestCase):
    section_name_empty = ""
    expected_error_empty = "Название раздела: Поле должно быть заполнено"

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.menu_page = RestaurantMenuPage(self.driver)
        self.menu_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_add_empty_new_section(self):
        self.menu_page.open_new_section_form()
        self.menu_page.set_section_name(self.section_name_empty)
        self.menu_page.save_section()
        error_msg = self.menu_page.get_section_name_error()
        self.assertEqual(error_msg, self.expected_error_empty)
