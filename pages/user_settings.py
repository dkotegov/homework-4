from helpers import Page
from components import Login, SideBar


class UserSettingsPage(Page):
    PATH = "user/profile"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def side_bar(self):
        return SideBar(self.driver)
