from pages.default import DefaultPage
from utils.helpers import wait_for_visible


class MainPage(DefaultPage):
    MOVIE_CARD = '.slider__card'
    VIEW_ALL_LINK = '.view-all'
    VIEW_ALL_FOR_GENRE = '#main-genre-search-button'
    GENRE_ITEM = '.genres-list__item-box'
    MOVIE_TITLE = '.title-box__title'
    PAGE_TITLE = '.main__page-title'
    MOVIE_RATING = '.right__movie-rating'
    MOVIE_CARD_TITLE = '.center__movie-link'
    MOVIE_CARD_POSTER = '.movie-card-img'

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

    def go_to_best_movies(self):
        wait_for_visible(self.driver, self.VIEW_ALL_LINK)
        self.driver.find_elements_by_css_selector(self.VIEW_ALL_LINK)[0].click()

    def get_page_title(self):
        wait_for_visible(self.driver, self.PAGE_TITLE)
        return self.driver.find_elements_by_css_selector(self.PAGE_TITLE)[0].text

    def select_genre(self, genre_name):
        wait_for_visible(self.driver, self.GENRE_ITEM)
        [item for item in self.driver.find_elements_by_css_selector(self.GENRE_ITEM) if item.text == genre_name][0]\
            .click()

    def go_to_movies_by_genre(self):
        wait_for_visible(self.driver, self.VIEW_ALL_FOR_GENRE)
        self.driver.find_element_by_css_selector(self.VIEW_ALL_FOR_GENRE).click()
        wait_for_visible(self.driver, self.PAGE_TITLE)

    def get_ratings(self):
        wait_for_visible(self.driver, self.MOVIE_RATING)
        return [item.text for item in self.driver.find_elements_by_css_selector(self.MOVIE_RATING)]

    def go_to_movie_via_title(self):
        wait_for_visible(self.driver, self.MOVIE_CARD_TITLE)
        self.driver.find_element_by_css_selector(self.MOVIE_CARD_TITLE).click()
        wait_for_visible(self.driver, self.MOVIE_TITLE)

    def go_to_movie_via_poster(self):
        wait_for_visible(self.driver, self.MOVIE_CARD_POSTER)
        self.driver.find_element_by_css_selector(self.MOVIE_CARD_POSTER).click()
        wait_for_visible(self.driver, self.MOVIE_TITLE)
