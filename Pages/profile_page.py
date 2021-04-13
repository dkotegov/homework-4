from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class ProfilePage(Page):
    PATH = '/profile'
    SUBSCRIBERS = '//a[text()="Подписки"]'
    USERNAME = '//span[@class="name__profile__default_margin--_Vkp5 name__profile_login--2W71f"]'

    def open_subscribers(self):
        self.open()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBERS)))
        self.driver.find_element_by_xpath(self.SUBSCRIBERS).click()

    def check_sub(self, path):
        self.open_subscribers()
        friend = '//a[@href="' + path + '"]'
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, friend)))

    def check_unsub(self, path):
        self.open_subscribers()
        friend = '//a[@href="' + path + '"]'
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, friend)))
        
    def check_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        username_in_profile = self.driver.find_element_by_xpath(self.USERNAME).text
        if username_in_profile == username:
            return True
        else:
            return False
