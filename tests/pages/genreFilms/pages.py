from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


CONTAINER = '.genres'

FILMS_BAR = '[class=genre-films-bar]'
FILM_FIRST = '[href^="/film?"]'

class Pages(BasePages):

    def wait_for_container():
        a.wait_for_load(css_locator=CONTAINER)

    def click_film():
        a.wait_for_load(css_locator=FILM_FIRST)
        element = a.find_element_by_css_selector(FILM_FIRST)
        element.click()

