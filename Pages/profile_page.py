from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

class ProfilePage(Page):
    PATH = '/profile'
    PLAYLIST = '//a[@id="play"]'
    PLAYLIST_INPUT = '//input[@class="name__input_main--1fQSy"]'
    PLAYLIST_BUTTON = '//button[text()="Создать"]'
    PLAYLIST_NAME = '//div[@class="name__filmlenta_genre--2DRas"]'
    PLAYLIST_DELETE = '//div[@class="name__delete--2d58m"][contains(@id, "playlist")]'
    FILM_DELETE = '//div[@class="name__delete--2d58m"][contains(@id, "poster")]'
    FILM_IN_PLAYLIST = '//a[@id="2"]'
    FILMS_IN_PLAYLIST = '//div[@class="name__lenta__object--3-XkZ"]'
    SUBSCRIBERS = '//a[@id="subscribe"]'
    ENTRY = '//button[text()="Войти"]'
    USERNAME = '//span[@class="name__profile__default_margin--_Vkp5 name__profile_login--2W71f"]'
    DELETE_USER = '//button[@id="deleteProfile"]'
    FRIEND = '//a[@href="people/17"]'
    FRIENDLIST = '//a[@class="name__friendList_login--gKHhK"]'
    DELETE_SUBSCRIBE = '//div[@id="profile/17"]'
    NOTIFICATION = '//span[@id="notification"]'


    def open_subscribers(self):
        self.open()
        self.driver.find_element_by_xpath(self.SUBSCRIBERS).click()

    def open_playlist(self):#+
        self.open()
        self.driver.find_element_by_xpath(self.PLAYLIST).click()

    def set_playlist(self, new):#+
        self.driver.find_element_by_xpath(self.PLAYLIST_INPUT).send_keys(new)

    def submit_playlist(self):#+
        self.driver.find_element_by_xpath(self.PLAYLIST_BUTTON).click()

    def wait_playlist_delete(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.PLAYLIST_NAME)))

    def wait_film_add(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FILM_IN_PLAYLIST)))

    def wait_film_delete(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.FILM_IN_PLAYLIST)))

    def get_last_playlist_name(self):#+
        return self.driver.find_elements_by_xpath(self.PLAYLIST_NAME)[-1].text

    def check_film_in_playlist(self):
        try:
            self.driver.find_element_by_xpath(self.FILM_IN_PLAYLIST)
        except NoSuchElementException:
            return False
        else:
            return True

    def get_count_playlist(self):#+-
        try:
            count = len(self.driver.find_elements_by_xpath(self.PLAYLIST_NAME))
        except NoSuchElementException:
            return 0
        else:
            return count


    def get_count_film_in_playlist(self):
        try:
            count = len(self.driver.find_elements_by_xpath(self.FILMS_IN_PLAYLIST))
        except NoSuchElementException:
            return 0
        else:
            return count - 1

    def delete_last_playlist(self):#+
        self.driver.find_elements_by_xpath(self.PLAYLIST_DELETE)[-1].click()

    def delete_film_from_playlist(self):#+
        self.driver.find_element_by_xpath(self.FILM_DELETE).click()

    def create_playlist(self, name):
        self.open_playlist()
        self.set_playlist(name)
        self.submit_playlist()
        self.driver.find_element_by_xpath(self.NOTIFICATION)
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.NOTIFICATION)))

    def get_subscribe_list(self):
        elements = self.driver.find_elements_by_xpath(self.FRIENDLIST)
        friends = []
        for element in elements:
            friends.append(element.text)
        return friends

    def unsubscribe_from_profile(self):
        self.driver.find_element_by_xpath(self.DELETE_SUBSCRIBE).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, self.FRIEND)))
        
    def check_username(self, username):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        username_in_profile = self.driver.find_element_by_xpath(self.USERNAME).text
        if username_in_profile == username:
            return True
        else:
            return False

    def get_username(self):
        return self.driver.find_element_by_xpath(self.USERNAME).text

    def delete_user(self):
        self.driver.find_element_by_xpath(self.DELETE_USER).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ENTRY)))

    def get_notification_text(self):
        return self.driver.find_element_by_xpath(self.NOTIFICATION).text

