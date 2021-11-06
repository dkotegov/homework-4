from helpers import Page
from components import SellerSideBar


class AchievementsPage(Page):
    PATH = "/user/1/achievements"

    def change_path(self, path):
        self.PATH = "/user/" + path + "/achievements"

    @property
    def side_bar(self):
        return SellerSideBar(self.driver)
