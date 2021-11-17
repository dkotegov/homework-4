import unittest

from faker import Faker
from tests.default_setup import default_setup
from tests.pages.restaurant.menu import RestaurantMenuPage
from tests.steps.auth_restaurant import auth_setup


class ChangeSectionSuccessTest(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        default_setup(self)
        auth_setup(self)
        self.menu_page = RestaurantMenuPage(self.driver)
        self.menu_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_add_new_section(self):
        section_name = self.fake.name()
        self.menu_page.open_new_section_form()
        self.menu_page.input_section_name(section_name)
        self.menu_page.save_section()
        sections = self.menu_page.get_all_sections_name()
        self.assertIn(section_name, sections)

    def test_delete_section(self):
        section_name = self.fake.name()
        self.menu_page.open_new_section_form()
        self.menu_page.set_section_name(section_name)
        self.menu_page.save_section()
        self.menu_page.open_delete_section_confirm(section_name)
        self.menu_page.delete_section_in_confirm()
        sections = self.menu_page.get_all_sections_name()
        self.assertNotIn(section_name, sections)

    def test_change_name_section(self):
        section_name = self.fake.name()
        change_section_name = self.fake.name()
        self.menu_page.open_new_section_form()
        self.menu_page.set_section_name(section_name)
        self.menu_page.save_section()
        self.menu_page.open_section_form(section_name)
        self.menu_page.set_section_name(change_section_name)
        self.menu_page.save_section()
        sections = self.menu_page.get_all_sections_name()
        self.assertIn(change_section_name, sections)
        self.assertNotIn(section_name, sections)
