from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


CONTAINER = '.genres'

FILMS_BAR = '[class=genre-films-bar]'
FILM_FIRST = '[href^="/film?"]'

GENRE_SECOND_BUTTON = '.nav-block__list div:nth-child(2)'

MORE_RES_BUTTON = '.js-more-res-button'

class Pages(BasePages):

    def wait_for_container():
        a.wait_for_load(css_locator=CONTAINER)

    def click_film():
        a.wait_for_load(css_locator=FILM_FIRST)
        element = a.find_element_by_css_selector(FILM_FIRST)
        element.click()

    def click_genre(): 
        a.wait_for_load(css_locator=GENRE_SECOND_BUTTON)
        element = a.find_element_by_css_selector(GENRE_SECOND_BUTTON)
        element.click()

    def click_more(): 
        a.wait_for_load(css_locator=MORE_RES_BUTTON)
        element = a.find_element_by_css_selector(MORE_RES_BUTTON)
        element.click()

    def count_films():
        element = a.find_elements_by_css_selector(FILM_FIRST)


