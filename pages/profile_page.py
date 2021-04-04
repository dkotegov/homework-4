from pages.base_page import Page
from pages.navbar import NavBar
from pages.profile_right_column import ProfileRightColumn


class ProfilePage(Page):
    PATH = '/profile'

    @property
    def navbar(self):
        return NavBar(self.driver)

    @property
    def right_column(self):
        return ProfileRightColumn(self.driver)
