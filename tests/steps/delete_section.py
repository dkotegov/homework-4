from tests.pages.restaurant.menu import RestaurantMenuPage


def delete_section_setup(t, section_name):
    menu_page = RestaurantMenuPage(t.driver)
    menu_page.open()
    menu_page.open_delete_section_confirm(section_name)
    menu_page.delete_section_in_confirm()
