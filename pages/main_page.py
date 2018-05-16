from components.main_vertical_list import MainVerticalList
from components.page import Page

from components.main_components import MainForm


class MainPage(Page):

    def open_friends_list(self):
        main_vertical_list = MainVerticalList(self.driver)
        main_vertical_list.get_friends().click()

    def my_name_surname(self):
        main_form = MainForm(self.driver)
        return main_form.get_name_surname()