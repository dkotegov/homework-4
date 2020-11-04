from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page


class AuthPage(Page):
    BASE_URL = 'https://mail.ru'
    PATH = ''

    LOGIN_INPUT = 'mailbox:login-input'
    SUBMIT_BUTTON = 'mailbox:submit-button'
    PASSWORD_INPUT = 'mailbox:password-input'
    LETTERS = 'dataset-letters'

    def login(self, email, password):
        driver = self.driver
        driver.find_element_by_id(self.LOGIN_INPUT).send_keys(email)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, self.PASSWORD_INPUT)))
        driver.find_element_by_id(self.PASSWORD_INPUT).send_keys(password)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.LETTERS)))
