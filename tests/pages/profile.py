from selenium.webdriver.common.by import By

from tests.pages.base import Page


class ProfilePage(Page):
    PATH = '/profile'
    ROOT = {
        'method': By.ID,
        'key': 'profile-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()
