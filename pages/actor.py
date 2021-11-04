from pages.default import Page
from utils import wait_for_element_by_selector

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ActorPage(Page):
    PATH = 'actors/'
    NAME_OF_ACTOR = '.name-born__name'
    FIRST_MOVIE_CARD = '.item__film-card:first-child'
    TITLE_OF_FIRST_MOVIE = '.item__film-card:first-child .item__film-card__title'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_name_of_actor(self):
        return wait_for_element_by_selector(self.driver, self.NAME_OF_ACTOR).text

    def click_on_first_movie(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.FIRST_MOVIE_CARD))
        )
        self.driver.find_element_by_css_selector(self.FIRST_MOVIE_CARD).click()

    def click_on_first_movie_name(self):
        wait_for_element_by_selector(self.driver, self.TITLE_OF_FIRST_MOVIE).click()


    def get_title_of_first_movie(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.TITLE_OF_FIRST_MOVIE))
        ).text