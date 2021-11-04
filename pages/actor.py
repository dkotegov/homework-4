from pages.default import Page
from utils import wait_for_element_by_selector


class ActorPage(Page):
    PATH = 'actors/'
    NAME_OF_ACTOR = '.name-born__name'
    FIRST_MOVIE_CARD = '.item__internal:first-child'
    TITLE_OF_FIRST_MOVIE = '.item__internal:first-child .item__suggestion__title'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_name_of_actor(self):
        return wait_for_element_by_selector(self.driver, self.NAME_OF_ACTOR).text

    def click_on_first_movie(self):
        wait_for_element_by_selector(self.driver, self.FIRST_MOVIE_CARD).click()

    def click_on_first_movie_name(self):
        wait_for_element_by_selector(self.driver, self.TITLE_OF_FIRST_MOVIE).click()

    def get_title_of_first_movie(self):
        return wait_for_element_by_selector(self.driver, self.TITLE_OF_FIRST_MOVIE).text
