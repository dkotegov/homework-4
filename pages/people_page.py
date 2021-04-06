from pages.base_page import Page
from pages.navbar import NavBar


class PeoplePage(Page):
    PATH = '/people'

    @property
    def navbar(self):
        return NavBar(self.driver)

    # TODO: add missing components
