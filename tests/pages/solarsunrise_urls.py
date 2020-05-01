from selenium.webdriver.common.by import By
from tests.pages.base import Page


class DefaultPage(Page):
    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()


class AuthPage(DefaultPage):
    PATH = '/login'
    ROOT = {
        'method': By.ID,
        'key': 'login-page'
    }


class RegPage(DefaultPage):
    PATH = '/'
    ROOT = {
        'method': By.ID,
        'key': 'signup-page'
    }


class ProfilePage(DefaultPage):
    PATH = '/profile'
    ROOT = {
        'method': By.ID,
        'key': 'profile-page'
    }

    # def __init__(self, driver, open=True):
    #     Page.__init__(self, driver)
    #     if open:
    #         self.open()


class SettingsPage(DefaultPage):
    PATH = '/settings'
    ROOT = {
        'method': By.ID,
        'key': 'settings-page'
    }


class IndexPage(DefaultPage):
    PATH = '/index/new'
    ROOT = {
        'method': By.ID,
        'key': 'index-page:new'
    }


class DialogPage(DefaultPage):
    PATH = '/dialog'
    ROOT = {
        'method': By.ID,
        'key': 'dialogview-page'
    }


class CreatePinPage(DefaultPage):
    PATH = '/create_pin'
    ROOT = {
        'method': By.ID,
        'key': 'createpin-page'
    }
