from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages

SEARCH_INPUT_QUERY = '#js-search-input'
SEARCH_BUTTON_ID = 'js-navbar-search'
SEARCH_RESULT_TITLE = '.search-results__film-card a:nth-child(1)'
SEARCH_RESULT_NOT_FOUND = '.profile__warning'

ADVANCED_SEARCH_BUTTON_ID = 'js-search-params'
ADVANCED_SEARCH_INPUT_GENRE_ID = 'js-genre-input'
ADVANCED_SEARCH_RESULTS = '.list__item'
ADVANCED_SEARCH_RESULT_GENRES_PART = 'a[href^="/search?genres='
FIRST_FILM = '[href^="/film?filmID="]'
FIRST_FILM_RATING = 'body > main > main > div.film-index > div.film > div.film__description > div:nth-child(2) > ' \
                    'div:nth-child(1)'
FILM_PAGE = '.film-index'
ADVANCED_SEARCH_INPUT_RATING_ID = 'js-ratingmin-input'
ADVANCED_SEARCH_INPUT_COUNTRY_ID = 'js-country-input'
FIRST_FILM_COUNTRY = '[href^="/search?countries="]'
ADVANCED_SEARCH_INPUT_YEAR_FROM_ID = 'js-yearmin-input'
ADVANCED_SEARCH_INPUT_YEAR_TO_ID = 'js-yearmax-input'
ADVANCED_SEARCH_RESULT_YEARS = 'a[href="search?year_min="]'


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

    @staticmethod
    def click_advanced_search_button():
        element = a.find_element_by_id(ADVANCED_SEARCH_BUTTON_ID)
        element.click()

    @staticmethod
    def enter_genre(genre):
        element = a.find_element_by_id(ADVANCED_SEARCH_INPUT_GENRE_ID)
        element.wait_and_click()
        element.send_keys(genre)

    @staticmethod
    def get_all_search_results_size():
        a.wait_for_load(css_locator=ADVANCED_SEARCH_RESULTS)
        return len(a.find_elements_by_css_selector(ADVANCED_SEARCH_RESULTS))

    @staticmethod
    def get_all_search_results_genres_size(genre):
        elements = a.find_elements_by_css_selector(ADVANCED_SEARCH_RESULT_GENRES_PART + genre + '"]')
        result = []
        for element in elements:
            result.append(element.get_text())
        return len(result)

    @staticmethod
    def get_first_film_rating():
        a.wait_for_load(css_locator=FIRST_FILM_RATING)
        element = a.find_element_by_css_selector(FIRST_FILM_RATING)
        return element.get_text()[-1]

    @staticmethod
    def click_first_film():
        new_window_url = a.find_element_by_css_selector(FIRST_FILM).get_attribute('href')
        a.get(new_window_url)

    @staticmethod
    def enter_rating(rating):
        element = a.find_element_by_id(ADVANCED_SEARCH_INPUT_RATING_ID)
        element.wait_and_click()
        element.send_keys(rating)

    @staticmethod
    def enter_country(country):
        element = a.find_element_by_id(ADVANCED_SEARCH_INPUT_COUNTRY_ID)
        element.wait_and_click()
        element.send_keys(country)

    @staticmethod
    def get_first_film_country():
        a.wait_for_load(css_locator=FIRST_FILM_COUNTRY)
        element = a.find_element_by_css_selector(FIRST_FILM_COUNTRY)
        return element.get_text()

    @staticmethod
    def enter_year_from(year_from):
        element = a.find_element_by_id(ADVANCED_SEARCH_INPUT_YEAR_FROM_ID)
        element.wait_and_click()
        element.send_keys(year_from)

    @staticmethod
    def enter_year_to(year_to):
        element = a.find_element_by_id(ADVANCED_SEARCH_INPUT_YEAR_TO_ID)
        element.wait_and_click()
        element.send_keys(year_to)

    @staticmethod
    def get_all_search_results_years():
        elements = a.find_elements_by_css_selector(ADVANCED_SEARCH_RESULT_YEARS)
        result = []
        for element in elements:
            result.append(int(element.get_text()[1:]))
        return result
