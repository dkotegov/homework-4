from pages.default import Page

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SeriesPage(Page):
    PATH = 'series/'
    TOP_SLIDER = '.container'
    FIRST_MOVIE_CARD = '.item__film-card:first-child'
    TITLE_OF_FIRST_MOVIE = '.item__film-card:first-child .item__film-card__title'
    GENRE_SLIDER = '.genres'
    FIRST_GENRE_CARD = '.genre-item:first-child'
    GENRE_NAME = 'data-genre'

    def click_on_first_genre(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.FIRST_GENRE_CARD))
        )
        self.driver.find_element_by_css_selector(self.FIRST_GENRE_CARD).click()

    def get_name_of_first_genre(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.FIRST_GENRE_CARD))
        ).get_attribute(self.GENRE_NAME)

    def click_on_first_movie(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.FIRST_MOVIE_CARD))
        )
        self.driver.find_element_by_css_selector(self.FIRST_MOVIE_CARD).click()

    def get_title_of_first_movie(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.TITLE_OF_FIRST_MOVIE))
        ).text

