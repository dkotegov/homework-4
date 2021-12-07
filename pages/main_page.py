from pages.default import DefaultPage
from utils.helpers import wait_for_visible


class MainPage(DefaultPage):
    MOVIE_CARD = '.slider__card'
    VIEW_ALL_LINK = '.view-all'
    GENRE_ITEM = '.genres-list__item-box'
    MOVIE_TITLE = '.title-box__title'

    def __init__(self, driver):
        super().__init__(driver, '/')

    def go_to_first_movie_page(self):
        wait_for_visible(self.driver, self.MOVIE_CARD)
        self.get_first_movie_card().click()
        wait_for_visible(self.driver, self.MOVIE_TITLE)

    def get_first_movie_card(self):
        wait_for_visible(self.driver, self.MOVIE_CARD)
        return self.driver.find_elements_by_css_selector(self.MOVIE_CARD)[0]

    def get_movie_card(self, title):
        wait_for_visible(self.driver, self.MOVIE_CARD)
        return self.driver.find_element_by_css_selector(f'[data-tooltip="{title}"]')

    def get_movie_title(self):
        wait_for_visible(self.driver, self.MOVIE_TITLE)
        return self.driver.find_element_by_css_selector(self.MOVIE_TITLE).text
