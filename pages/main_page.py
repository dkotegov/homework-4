from components.main_up_toolbar import MainUpToolbar
from components.main_vertical_list import MainVerticalList
from components.page import Page


class MainPage(Page):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.main_up_toolbar = MainUpToolbar(self.driver)
        self.main_vertical_list = MainVerticalList(self.driver)

    def open_friends_list(self):
        self.main_vertical_list.get_friends().click()

    def open_games_list(self):
        self.main_vertical_list.get_games().click()

    def open_notification(self):
        self.main_up_toolbar.get_notification().click()
        # self.main_up_toolbar.get_notification_games().click()

    def check_notification(self):
        image_element = self.main_up_toolbar.get_image_element()
        if image_element is False:
            return False
        if image_element == self.main_up_toolbar.get_element_by_id():
            return image_element




