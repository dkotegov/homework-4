import constants
from pages.default import Page
from utils import wait_for_element_by_selector


class FavouritesPage(Page):
    PATH = 'favourite'
    HREF = 'href'
    FIRST_FAVOURITE_MOVIE = '.item__internal:first-child'

    def get_id_of_first_fav_movie(self):
        href = wait_for_element_by_selector(self.driver, self.FIRST_FAVOURITE_MOVIE).get_attribute(self.HREF)
        return href[constants.LEN_OF_HREF_WITHOUT_ID:]

    def is_has_favourites(self):
        try:
            wait_for_element_by_selector(self.driver, self.FIRST_FAVOURITE_MOVIE)
            return True
        except:
            return False