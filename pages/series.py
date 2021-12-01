from pages.default import Page

from utils import wait_click_for_element_by_selector, wait_for_element_by_selector

class SeriesPage(Page):
    PATH = 'series/'
    TOP_SLIDER = '.container'
    FIRST_MOVIE_CARD = '.item__film-card:first-child'
    TITLE_OF_FIRST_MOVIE = '.item__film-card:first-child .item__film-card__title'
    GENRE_SLIDER = '.genres'
    FIRST_GENRE_CARD = '.genre-item:first-child'
    GENRE_NAME = 'data-genre'

    def click_on_first_genre(self):
        wait_click_for_element_by_selector(self.driver, self.FIRST_GENRE_CARD)

    def get_name_of_first_genre(self):
        return wait_for_element_by_selector(self.driver, self.FIRST_GENRE_CARD).get_attribute(self.GENRE_NAME)

    def click_on_first_movie(self):
        wait_click_for_element_by_selector(self.driver, self.FIRST_MOVIE_CARD)

    def get_title_of_first_movie(self):
        return wait_for_element_by_selector(self.driver, self.TITLE_OF_FIRST_MOVIE).text

