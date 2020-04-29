from tests.conftest import accessor as a
from tests.pages.search.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_advanced_search_page():
        a.driver.get('https://cinsear.ru/search')

    @staticmethod
    def enter_search_query(query):
        Pages.enter_search_query(query)
        Pages.click_search_button()

    @staticmethod
    def check_search_result_title(expected_title_part):
        title = Pages.get_first_film_title()
        assert title.lower().startswith(expected_title_part.lower())

    @staticmethod
    def check_search_result_not_found():
        Pages.find_not_found_message()
