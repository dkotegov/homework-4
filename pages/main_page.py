from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = '/'

    def __init__(self, driver):
        super().__init__(driver, '#messages-page')

    def get_authenticated_user_email(self):
        return self.locate_el('#profile-link-username').text
