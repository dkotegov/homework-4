from pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    PATH = '/user/{}/password'

    def __init__(self, driver, username):
        super().__init__(driver, 'div.profile')
        self.PATH = self.PATH.format(username)
