from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class SettingPage(Page):
    AVATAR_PATH = os.getcwd() + '/media/vorobey.jpg'
    AVATAR_INPUT = '//input[@name="file"]'
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/profileChange'
    USERNAME = '//input[@name="login"]'
    OLD = '//input[@placeholder="Старый пароль"]'
    NEW = '//input[@placeholder="Новый пароль"]'
    REPEAT = '//input[@placeholder="Повторите новый пароль"]'
    SUBMIT = '//button[text()="Сохранить"]'
    ERROR_MSG_MAIN = '//div[@id="badMain"]'
    ERROR_MSG_PASSWORD = '//div[@id="badNewPassword"]'
    ERROR_MSG_DIFFERENT_NEW = '//div[@id="differentPassword"]'
    NOTIFICATION = '//span[@id="notification"]'


    def set_old_pass(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new_pass(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)

    def set_new_pass_confirm(self, new):
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_main_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_MAIN).text

    def get_password_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_PASSWORD).text

    def get_password_diff_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_DIFFERENT_NEW).text

    def get_notification_text(self):
        return self.driver.find_element_by_xpath(self.NOTIFICATION).text

    ''''''

    def change_password(self, old, new, new_conf):
        self.set_old_pass(old)
        self.set_new_pass(new)
        self.set_new_pass_confirm(new_conf)
        self.submit()

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.USERNAME).send_keys(username)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def change_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        self.set_username(username)
        self.submit()

    def change_username_less_5_symbol(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        self.set_username("1234")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ERROR_USERNAME_LESS_5)))

    def setup_avatar(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.AVATAR_INPUT)))
        self.driver.find_element_by_xpath(self.AVATAR_INPUT).send_keys(self.AVATAR_PATH)
        return self.driver.find_element_by_xpath(self.AVATAR_INPUT).get_attribute("value")

