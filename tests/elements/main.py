# coding=utf-8
import time

from selenium.webdriver.common.by import By

from base import BaseElement


class MainElements(BaseElement):

    def user_email(self):
        self.locator = (By.XPATH, "//span[@id='PH_authMenu_button']")
        return self

    def send_message_elem(self):
        self.locator = (By.XPATH, "//span[text() = 'Написать письмо']")
        return self

    def sent_message_elem(self):
        self.locator = (By.XPATH, "//span[text() = 'Отправленные']")
        return self

    def recieve_elem(self):
        self.locator = (By.XPATH, "//span[text() = 'Входящие']")
        return self

    def delete_elem(self):
        self.locator = (By.XPATH, "(//div[@id='ScrollBody']//span[text()='Удалить'])[1]")
        return self

    def subject_elem(self):
        self.locator = (By.XPATH, "//div[@class='b-letter__head__subj__text']")
        return self

    def to_elem(self):
        self.locator = (By.XPATH, "//span[@class='b-letter__head__addrs__value']")
        return self

    def text_elem(self):
        self.locator = (By.XPATH, "//div[@class='b-letter__body']")
        return self

    def last_message_elem(self):
        self.locator = (By.XPATH, "(//div[@class='b-datalist b-datalist_letters b-datalist_letters_to'])//div[@data-bem='b-datalist__item'][1]")
        return self

    def last_checkbox(self):
        self.locator = (By.XPATH, "(//div[@class='b-datalist b-datalist_letters b-datalist_letters_to'])//div[@data-bem='b-datalist__item'][1]//div[@class='js-item-checkbox b-datalist__item__cbx']")
        return self

    def last_recieve_elem(self):
        self.locator = (By.XPATH, "(//div[@class='b-datalist b-datalist_letters b-datalist_letters_from'])//div[@data-bem='b-datalist__item'][1]") 
        return self

    def last_recieve_checkbox(self):
        self.locator = (By.XPATH, "(//div[@class='b-datalist b-datalist_letters b-datalist_letters_from'])//div[@data-bem='b-datalist__item'][1]//div[@class='js-item-checkbox b-datalist__item__cbx']")
        return self