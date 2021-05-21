from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class PeoplePage(Page):
    PATH = '/people/17'
    SUBSCRIBE_BUTTON = '//button[text()="Подписаться"]'
    UNSUBSCRIBE_BUTTON = '//button[text()="Отписаться"]'

    def subscribe(self):
        self.open()
        self.driver.find_element_by_xpath(self.SUBSCRIBE_BUTTON).click()

    def unsubscribe(self):
        self.open()
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_BUTTON).click()

