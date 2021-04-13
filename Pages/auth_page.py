from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class AuthPage(Page):
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/login'
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@class="name__button--2Ten8 name__buttons__marginForFilmCard--29k8-"]'
    ICON = '//img[@class="name__round--21Oxj"]'

    def set_login(self):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(self.USERNAME_INPUT)

    def set_password(self):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(self.PASSWORD_INPUT)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def auth(self):
        self.open()
        self.set_login()
        self.set_password()
        self.submit()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ICON)))
