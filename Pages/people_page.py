from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class PeoplePage(Page):
    PATH = '/people/17'
    SUBSCRIBE_BUTTON = '//button[text()="Подписаться"]'
    UNSUBSCRIBE_BUTTON = '//button[text()="Отписаться"]'

    def subscribe(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBE_BUTTON)))
        self.driver.find_element_by_xpath(self.SUBSCRIBE_BUTTON).click()
        WebDriverWait(self.driver, 10, 2).until(EC.presence_of_element_located((By.XPATH, self.UNSUBSCRIBE_BUTTON)))

    def unsubscribe(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.UNSUBSCRIBE_BUTTON)))
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_BUTTON).click()
        WebDriverWait(self.driver, 10, 2).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBE_BUTTON)))

    def sub_and_unsub(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBE_BUTTON)))
        self.driver.find_element_by_xpath(self.SUBSCRIBE_BUTTON).click()
        WebDriverWait(self.driver, 10, 2).until(EC.presence_of_element_located((By.XPATH, self.UNSUBSCRIBE_BUTTON)))
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_BUTTON).click()
        WebDriverWait(self.driver, 10, 2).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBE_BUTTON)))

