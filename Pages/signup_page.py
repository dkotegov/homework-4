from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SignupPage(Page):
    PATH = '/signup'
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    MAIL = '//input[@name="email"]'
    SUBMIT = '//button[text()="Регистрация"]'
    ICON = '//img[@class="name__round--21Oxj"]'
    ERROR_MSG = '//div[@class="name__error--FQ9hR"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_mail(self, mail):
        self.driver.find_element_by_xpath(self.MAIL).send_keys(mail)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def wait_for_account(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ICON)))

    def get_error_bad_fields(self):
        return self.driver.find_elements_by_xpath(self.ERROR_MSG)[2].text

    def get_error_bad_login(self):
        return self.driver.find_elements_by_xpath(self.ERROR_MSG)[0].text

    def get_error_bad_password(self):
        return self.driver.find_elements_by_xpath(self.ERROR_MSG)[1].text
