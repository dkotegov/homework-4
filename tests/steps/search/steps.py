from selenium.common.exceptions import StaleElementReferenceException

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
        try:
            Pages.enter_genre(genre)
        except StaleElementReferenceException:
            Pages.enter_genre(genre)

    @staticmethod
    def click_advance_search():
        try:
            Pages.click_advanced_search_button()
        except StaleElementReferenceException:
            Pages.click_advanced_search_button()

    @staticmethod
    def check_first_film_genre(genre):
        Pages.find_first_film_genre(genre)

    @staticmethod
    def check_first_film_rating(rating_from):
        Pages.click_first_film()
        assert int(rating_from) <= int(Pages.get_first_film_rating())

    @staticmethod
    def enter_rating(rating):
        try:
            Pages.enter_rating(rating)
        except StaleElementReferenceException:
            Pages.enter_rating(rating)

    @staticmethod
    def enter_country(country):
        try:
            Pages.enter_country(country)
        except StaleElementReferenceException:
            Pages.enter_country(country)

    @staticmethod
    def check_first_film_country(country):
        Pages.click_first_film()
        assert Pages.get_first_film_country().lower() in country.lower()

    @staticmethod
    def enter_years(year_from, year_to):
        try:
            Pages.enter_year_from(year_from)
        except StaleElementReferenceException:
            Pages.enter_year_from(year_from)
        try:
            Pages.enter_year_to(year_to)
        except StaleElementReferenceException:
            Pages.enter_year_to(year_to)

    @staticmethod
    def check_first_film_year(year_from, year_to):
        year = Pages.get_first_film_year()
        assert int(year_from) <= year <= int(year_to)
