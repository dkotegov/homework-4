from pages.BasePage import Page
from pages.NavBar import NavBar


class MeetingsPage(Page):
    PATH = '/meetings'

    @property
    def navbar(self):
        return NavBar(self.driver)

    # TODO: add missing components
