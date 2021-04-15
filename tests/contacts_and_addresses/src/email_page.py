from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tests.contacts_and_addresses.page_component import Page, Component


class EmailPage(Page):
    PATH = ''

    @property
    def form(self):
        return EmailForm(self.driver)


class EmailForm(Component):
    ADD_EMAIL = '//*[@data-test-id="recovery-addEmail-button"]'
    EMAIL_INPUT = '//*[@data-test-id="recovery-addEmail-emailField-input"]'
    CANCEL = '//*[@data-test-id="recovery-addEmail-cancel"]'
    CANCEL_DELETE = '//*[@data-test-id="recovery-deleteEmail-cancel"]'
    EMAIL_SUBMIT = '//*[@data-test-id="recovery-addEmail-submit"]'
    CHECK_EMAIL = '//*[@data-test-id="recovery-email-wrapper"]'
    DELETE_EMAIL = '//*[@data-test-id="recovery-delete-email-button"]'
    DELETE_SUBMIT = '//*[@data-test-id="recovery-deleteEmail-submit"]'
    CLOSE = '//*[@data-test-id="recovery-success-close"]'
    ERROR = '//*[@data-test-id="error-footer-text"]'
    Invalid_email = '//*[@data-test-id="recovery-error-invalidEmail"]'
    test_mail = 'test.michael@mail.ru'

    def open_adding(self):
        self.next_button_click(self.ADD_EMAIL)

    def add_email(self, text):
        self.next_button_click(self.ADD_EMAIL)
        self.input_email(text)
        self.next_button_click(self.EMAIL_SUBMIT)

    def check_error(self):
        text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.Invalid_email)
        )
        return text.text

    def get_success(self):
        text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHECK_EMAIL)
        )
        return text.text

    def close_success(self):
        self.next_button_click(self.CLOSE)

    def input_email(self, text):
        input_text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EMAIL_INPUT)
        )
        input_text.send_keys(text)

    def next_button_click(self, name):
        next_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(name)
        )
        next_button.click()

    def cancel(self):
        cancel_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CANCEL)
        )
        cancel_button.click()

    def cancel_delete(self):
        self.next_button_click(self.DELETE_EMAIL)
        self.next_button_click(self.CANCEL_DELETE)

    def delete_email(self):
        self.next_button_click(self.DELETE_EMAIL)
        self.next_button_click(self.DELETE_SUBMIT)
