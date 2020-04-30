from selenium.webdriver.support.select import Select

from tests.conftest import accessor
from tests.pages.base.base_pages import BasePages


class Pages(BasePages):
    @staticmethod
    def select_list(list_name):
        selector = '.js-select'
        accessor.sleep(1)
        accessor.wait_for_load(css_locator=selector)
        select = Select(accessor.find_element_by_css_selector(selector).element)
        select.select_by_visible_text(list_name)

    @staticmethod
    def enter_new_list_name(list_name):
        element_id = 'js-list-input'
        accessor.wait_for_load(id_locator=element_id)
        element = accessor.find_element_by_id(element_id)
        element.send_keys(list_name)

    @staticmethod
    def save_new_list():
        element_id = 'js-create-list'
        accessor.wait_for_load(id_locator=element_id)
        element = accessor.find_element_by_id(element_id)
        element.click()
