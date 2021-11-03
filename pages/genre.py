from pages.default import Page
from utils import wait_for_element_by_selector


class GenrePage(Page):
    GENRE_NAME = '.item__page-title'

    def get_genre_name(self):
        return wait_for_element_by_selector(self.driver, self.GENRE_NAME).text
