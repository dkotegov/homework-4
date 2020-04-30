from selenium.webdriver.common.by import By
from tests.pages.base import Page


class AuthPage(Page):
    PATH = '/login'
    ROOT = {
        'method': By.ID,
        'key': 'login-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()


class RegPage(Page):
    PATH = '/'
    ROOT = {
        'method': By.ID,
        'key': 'signup-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()


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


class SettingsPage(Page):
    PATH = '/settings'
    ROOT = {
        'method': By.ID,
        'key': 'settings-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()
