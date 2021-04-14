from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os


class FilmPage(Page):
    PATH = '/film/1'
    ADD_BUTTON = '//button[@id="adding"]'
    NOTIFICATION_SUCCESS = '//div[@class="name__notificationSuccess--2LyUD"]'
    NOTIFICATION_EXIST = '//div[@class="name__notificationFail--15d1Q"]'

    def add_film_in_playlist(self):
        self.open()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ADD_BUTTON)))
        self.driver.find_element_by_xpath(self.ADD_BUTTON).click()

    def check_adding_in_playlist_succes(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.NOTIFICATION_SUCCESS)))
        try:
            self.driver.find_elements_by_xpath(self.NOTIFICATION_SUCCESS)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_adding_in_playlist_exist(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.NOTIFICATION_EXIST)))
        try:
            self.driver.find_elements_by_xpath(self.NOTIFICATION_EXIST)
        except NoSuchElementException:
            return False
        else:
            return True
