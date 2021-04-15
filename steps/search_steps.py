from pages.meetings_page import MeetingsPage
from pages.search_block import SearchBlock
from steps.base_steps import Steps


class SearchSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = MeetingsPage(driver)
        self.search_block = SearchBlock(driver)

    def open_search_block(self):
        self.page.navbar.click_search()

    def get_search_offers(self):
        return self.search_block.get_search_offers()

    def enter_search_query(self, query):
        self.search_block.enter_search_query(query)