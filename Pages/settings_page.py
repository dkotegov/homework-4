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
    ERROR_WRONG_OLD = '//div[text()="\nНеправильный старый пароль"][@class="name__error--FQ9hR"]'
    ERROR_DIFF_NEW = '//div[text()="Пароли не совпадают"][@class="name__error--FQ9hR"]'
    ERROR_USERNAME_LESS_5 = '//div[text()="Недопустимый логин(Должен быть от 5 до 15 символов)"][@class="name__error--FQ9hR"]'
    ERROR_USERNAME_EXIST = '//div[text()="\nПользователь с таким логином уже существует"][@class="name__error--FQ9hR"]'

    def set_old_pass(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new_pass(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)

    def set_new_pass_confirm(self, new):
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.USERNAME).send_keys(username)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def change_pass(self, old, new, new_conf):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.OLD)))
        self.set_old_pass(old)
        self.set_new_pass(new)
        self.set_new_pass_confirm(new_conf)
        self.submit()

    def change_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        self.set_username(username)
        self.submit()

    def change_username_less_5_symbol(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        self.set_username("1234")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ERROR_USERNAME_LESS_5)))

    def setup_avatar(self):
        self.driver.find_element_by_xpath(self.AVATAR_INPUT).send_keys(self.AVATAR_PATH)

    def get_avatar_text(self):
        return self.driver.find_element_by_xpath(self.AVATAR_INPUT).get_attribute("value")

