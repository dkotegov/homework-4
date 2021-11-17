from tests.pages.restaurant.menu import RestaurantMenuPage
from faker import Faker


def add_section_setup(t):
    fake = Faker()
    section_name = fake.name()
    menu_page = RestaurantMenuPage(t.driver)
    menu_page.open()
    menu_page.open_new_section_form()
    menu_page.set_section_name(section_name)
    menu_page.save_section()
    return section_name
