from pages.default import Page
from utils import wait_for_element_by_selector


class ProfilePage(Page):
    PATH = 'profile/'
    TITLE = '.title-wrapper__title'

    def get_title_of_page(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text
