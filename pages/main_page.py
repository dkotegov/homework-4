from components.main_vertical_list import MainVerticalList
from components.page import Page


class MainPage(Page):

    def open_friends_list(self):
        main_vertical_list = MainVerticalList(self.driver)
        main_vertical_list.get_friends().click()