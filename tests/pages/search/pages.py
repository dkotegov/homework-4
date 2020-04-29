from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


SEARCH_INPUT_QUERY = 'js-search-input'
SEARCH_BUTTON_ID = 'js-navbar-search'
SEARCH_RESULT_TITLE = '.search-results__film-card a:nth-child(1)'
SEARCH_RESULT_NOT_FOUND = '.profile__warning'


class Pages(BasePages):
    @staticmethod
    def enter_search_query(query):
        element = a.find_element_by_id(SEARCH_INPUT_QUERY)
        element.wait_and_click()
        element.send_keys(query)

    @staticmethod
    def click_search_button():
        element = a.find_element_by_id(SEARCH_BUTTON_ID)
        element.click()

    @staticmethod
    def get_first_film_title():
        a.wait_for_load(css_locator=SEARCH_RESULT_TITLE)
        element = a.find_element_by_css_selector(SEARCH_RESULT_TITLE)
        return element.get_text()

    @staticmethod
    def find_not_found_message():
        a.wait_for_load(css_locator=SEARCH_RESULT_NOT_FOUND)
