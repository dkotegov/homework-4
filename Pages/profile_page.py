from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class ProfilePage(Page):
    PATH = '/profile'
    SUBSCRIBERS = '//a[text()="Подписки"]'

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
