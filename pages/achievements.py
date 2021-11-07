from consts import TEST_USER
from helpers import Page
from components import SellerSideBar


class AchievementsPage(Page):
    PATH = "/user/{}/achievements".format(TEST_USER)

    PAGE = ".achievement"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def change_path(self, path):
        self.PATH = "/user/" + path + "/achievements"

    @property
    def side_bar(self):
        return SellerSideBar(self.driver)
