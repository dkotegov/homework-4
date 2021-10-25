from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'div.signup')
