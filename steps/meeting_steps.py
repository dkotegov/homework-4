from pages.meeting_page import MeetingPage
from steps.base_steps import Steps


class MeetingSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = MeetingPage(driver)

    def click_like(self):
        self.page.click_like_icon()

    def click_go_button(self):
        self.page.click_go_button()

    def click_meet_member(self):
        self.page.click_meet_member()

    def handle_like(self):
        self.page.handle_like()

    def handle_go_button(self):
        self.page.handle_go_button()