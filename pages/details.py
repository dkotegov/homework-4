from pages.default import Page
from utils import wait_for_element_by_selector


class DetailsPage(Page):
    PATH = 'movie/'
    TITLE = '.detail-preview__title'
    TRANSITION_STUB = '.sub__href'
    LAST_ACTOR = '.actors__href:last-child'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_title(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text

    def transit_by_stub(self):
        wait_for_element_by_selector(self.driver, self.TRANSITION_STUB).click()

    def click_on_last_actor(self):
        wait_for_element_by_selector(self.driver, self.LAST_ACTOR).click()

    def get_name_of_last_actor(self):
        return wait_for_element_by_selector(self.driver, self.LAST_ACTOR).text
