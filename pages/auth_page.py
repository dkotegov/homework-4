import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.page import Page


class AuthPage(Page):
    BASE_URL = 'https://mail.ru'
    PATH = ''

    EMAIL = 'a.seledkina_test@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    LOGIN_INPUT = 'mailbox:login-input'
    SUBMIT_BUTTON = 'mailbox:submit-button'
    PASSWORD_INPUT = 'mailbox:password-input'
    LETTERS = 'dataset-letters'

    def login(self):
        driver = self.driver
        driver.find_element_by_id(self.LOGIN_INPUT).send_keys(self.EMAIL)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, self.PASSWORD_INPUT)))
        driver.find_element_by_id(self.PASSWORD_INPUT).send_keys(self.PASSWORD)
        driver.find_element_by_id(self.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.LETTERS)))
