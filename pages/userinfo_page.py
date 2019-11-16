import os

from pages.default_page import DefaultPage, Component
from helpers import wait_for_element


class UserinfoPage(DefaultPage):
    URL = 'https://e.mail.ru/settings/userinfo'

    @property
    def form(self):
        return UserinfoForm(self.driver)


class UserinfoForm(Component):
    TOWN = 'input[name="your_town"]'
    SURNAME = 'input[name="LastName"]'            
    SAVE = 'div.form__actions__inner button[type="submit"]'
    TOP_MESSAGE = 'div.content__page > div.form__top-message.form__top-message_error > span'
    TOWN_ERROR = 'input[name="your_town"] ~ .form__message.form__message_error'

    def set_town(self, town):
        wait_for_element(self.driver, self.TOWN)
        self.driver.find_element_by_css_selector(self.TOWN).send_keys(town)

    def save(self):
        wait_for_element(self.driver, self.SAVE)
        self.driver.find_element_by_css_selector(self.SAVE).click()

    def get_top_message(self):
        wait_for_element(self.driver, self.TOP_MESSAGE)
        return self.driver.find_element_by_css_selector(self.TOP_MESSAGE).text

    def get_town_message(self):
        wait_for_element(self.driver, self.TOWN_ERROR)
        return self.driver.find_element_by_css_selector(self.TOWN_ERROR).text
