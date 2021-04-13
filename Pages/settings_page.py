from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class SettingPage(Page):
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/profileChange'
    OLD = '//input[@placeholder="Старый пароль"]'
    NEW = '//input[@placeholder="Новый пароль"]'
    REPEAT = '//input[@placeholder="Повторите новый пароль"]'
    SUBMIT = '//button[text()="Сохранить"]'
    ERROR_WRONG_OLD = '//div[text()="\nНеправильный старый пароль"][@class="name__error--FQ9hR"]'
    ERROR_DIFF_NEW = '//div[text()="Пароли не совпадают"][@class="name__error--FQ9hR"]'

    def set_old_pass(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new_pass(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)

    def set_new_pass_confirm(self, new):
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def change_pass(self, old, new, new_conf):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.OLD)))
        self.set_old_pass(old)
        self.set_new_pass(new)
        self.set_new_pass_confirm(new_conf)
        self.submit()

