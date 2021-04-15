from selenium.webdriver.support.ui import WebDriverWait
from tests.contacts_and_addresses.page_component import Page, Component
import urllib.parse as urlparse


class PhonePage(Page):
    PATH = ''

    @property
    def form(self):
        return PhoneForm(self.driver)


class PhoneForm(Component):
    ADD_NUMBER = '//*[@data-test-id="recovery-addPhone-button"]'
    Phone_Select = '//*[@data-test-id="country-select"]'
    KAZAH = '//*[@data-test-id="select-value:kz"]'
    Path = 'https://id.mail.ru/contacts'
    CANCEL = '//*[@data-test-id="recovery-addPhone-cancel"]'

    def add_number(self):
        self.next()
        select = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.Phone_Select)
        )
        select.click()
        self.driver.find_element_by_xpath(self.KAZAH).click()
        self.cancel()

    def next(self):
        next_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ADD_NUMBER)
        )
        next_button.click()

    def cancel(self):
        cancel_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CANCEL)
        )
        cancel_button.click()
