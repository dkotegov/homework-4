from pages.people_page import PeoplePage
from steps.base_steps import Steps


class PeopleSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = PeoplePage(driver)

    def click_disguisht(self):
        self.page.click_disguisht()

    def click_like_icon(self):
        self.page.click_like_icon()

    def click_download_more(self):
        self.page.click_download_more()
    
    def handle_like(self):
        self.handle_like()