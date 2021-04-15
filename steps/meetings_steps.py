from pages.meetings_page import MeetingsPage
from steps.base_steps import Steps


class MeetingsSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = MeetingsPage(driver)

    def click_card(self):
        self.page.click_card()

    def click_slide(self):
        self.page.click_slide()

    def like_card(self):
        self.page.click_card_like()

    def like_slide(self):
        self.page.click_slide_like()

    def go_button(self):
        self.page.click_slide_go_button()

    def click_my_meetings(self):
        self.page.click_my_meetings()

    def click_disguisht(self):
        self.page.click_disguisht()

    def click_remove_filters(self):
        self.page.click_remove_filters()

    def wait_page_load(self, url):
        self.page.wait_page_load(url)

    def handle_go_button(self):
        self.page.wait_for_go_update_confirmation()
    
    def handle_like(self):
        self.page.wait_for_like_update_confirmation()