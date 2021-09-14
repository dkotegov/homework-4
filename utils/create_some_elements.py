import os

from pages.load_page import HomePage


def create_elements(t, names):
    home_page = HomePage(t.driver)
    for name in names:
        elements = home_page.take_all_elements()
        elements[0].click()
        home_page.create_folder_home_page()
        home_page.input_info(name)
        home_page.click_create()
        home_page.open_cloud()


def delete_elements(t):
    home_page = HomePage(t.driver)
    home_page.open_cloud()
    home_page.take_all_highlight()
    home_page.del_elements()
    home_page.click_button_delete()
    home_page.wait()


def upload_elements(t):
    home_page = HomePage(t.driver)
    home_page.click_close_dialog()
    list_file = os.listdir('data')
    for name_file in list_file:
        home_page.click_upload()
        home_page.input_file(name_file)
        home_page.wait_load()


def favorite_add(t, elements_list):
    home_page = HomePage(t.driver)
    elem = home_page.open_drop_menu(elements_list[1])
    home_page.add_to_favorite()
    home_page.check_favorite(elem, True)


def base_view(t):
    home_page = HomePage(t.driver)
    home_page.click_view()
    home_page.select_view_table()
    home_page.click_sort()
    home_page.select_sort_alfa()
