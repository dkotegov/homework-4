from components.black_list import BlackList
from components.page import Page


class BlackListPage(Page):
    PAGE = '/blacklist'

    def delete_from(self):
        black_list = BlackList(self.driver)
        black_list.get_delete_button().click()
        black_list.get_confirm_button().click()