import os
from selenium.webdriver.support.ui import WebDriverWait

from pages.page import Page


class AuthPage(Page):
    BASE_URL = 'https://mail.ru'
    PATH = ''

    EMAIL = 'a.seledkina_test@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    LOGIN_INPUT = 'mailbox:login-input'
    SUBMIT_BUTTON = 'mailbox:submit-button'
    PASSWORD_INPUT = 'mailbox:password-input'
    USER_EMAIL_LINK = 'PH_user-email'

    def login(self):
        driver = self.driver
        driver.find_element_by_id(self.LOGIN_INPUT).send_keys(self.EMAIL)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        driver.find_element_by_id(self.PASSWORD_INPUT).send_keys(self.PASSWORD)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id(self.USER_EMAIL_LINK).text == self.EMAIL)
