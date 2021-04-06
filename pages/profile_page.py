from pages.base_page import Page
from pages.navbar import NavBar
from pages.profile_left_column import ProfileLeftColumn
from pages.profile_right_column import ProfileRightColumn


class ProfilePage(Page):
    PATH = '/profile'

    @property
    def navbar(self):
        return NavBar(self.driver)

    @property
    def right_column(self):
        return ProfileRightColumn(self.driver)

    @property
    def left_column(self):
        return ProfileLeftColumn(self.driver)
