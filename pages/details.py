import urllib.parse

from pages.default import Page
from utils import wait_for_element_by_selector


class DetailsPage(Page):
    PATH = 'movie/'
    TITLE = '.detail-preview__title'
    TRANSITION_TO_AUTH_PAGE = '.sub__href'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_title(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text

    def transit_to_auth_page(self):
        wait_for_element_by_selector(self.driver, self.TRANSITION_TO_AUTH_PAGE).click()
