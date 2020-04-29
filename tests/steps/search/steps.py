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

    @staticmethod
    def enter_genre(genre):
        Pages.enter_genre(genre)

    @staticmethod
    def click_advance_search():
        Pages.click_advanced_search_button()

    @staticmethod
    def check_all_search_result_genre(genre):
        all_search_results_size = Pages.get_all_search_results_size()
        assert all_search_results_size > 0
        assert all_search_results_size == Pages.get_all_search_results_genres_size(genre)

    @staticmethod
    def check_first_film_rating(rating_from):
        all_search_results_size = Pages.get_all_search_results_size()
        assert all_search_results_size > 0
        Pages.click_first_film()
        assert int(rating_from) <= int(Pages.get_first_film_rating())

    @staticmethod
    def enter_rating(rating):
        Pages.enter_rating(rating)

    @staticmethod
    def enter_country(country):
        Pages.enter_country(country)

    @staticmethod
    def check_first_film_country(country):
        all_search_results_size = Pages.get_all_search_results_size()
        assert all_search_results_size > 0
        Pages.click_first_film()
        assert Pages.get_first_film_country().lower() in country.lower()

    @staticmethod
    def enter_years(year_from, year_to):
        Pages.enter_year_from(year_from)
        Pages.enter_year_to(year_to)

    @staticmethod
    def check_all_search_result_year(year_from, year_to):
        all_search_results_size = Pages.get_all_search_results_size()
        assert all_search_results_size > 0
        years = Pages.get_all_search_results_years()
        for year in years:
            assert year_from <= year <= year_to
