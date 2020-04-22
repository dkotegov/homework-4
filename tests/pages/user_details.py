from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class UserDetailsPage(Page):
    PATH = '/users/{0}'

    ROOT = {
        'method': By.ID,
        'key': 'user-page'
    }

    def __init__(self, driver, nickname):
        Page.__init__(self, driver)
        self.open(nickname)

    @property
    def form(self):
        return UserDetailsSubscribeForm(self.driver)


class UserDetailsSubscribeForm(FormComponent):
    subscribe_button = '//input[@class="button-subscribe"]'
    unsubscribe_button = '//input[@class="button-already-subscribe"]'

    def subscribe(self):
        self.driver.find_element_by_xpath(self.subscribe_button).click()
        self.wait_for_presence(By.XPATH, self.unsubscribe_button)

    def unsubscribe(self):
        self.driver.find_element_by_xpath(self.unsubscribe_button).click()
        self.wait_for_presence(By.XPATH, self.subscribe_button)




