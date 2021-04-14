from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_expected_conditions import presence_number_of_elements as customEC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os


class FilmPage(Page):
    PATH = '/film/1'
    ADD_BUTTON = '//button[@id="adding"]'
    NOTIFICATION_SUCCESS = '//div[@class="name__notificationSuccess--2LyUD"]'
    NOTIFICATION_EXIST = '//div[@class="name__notificationFail--15d1Q"]'
    COMMENT_AREA = '//textarea[@id="msg"]'
    SUBMIT_COMMENT = '//button[@id="msg_button"]'
    COMMENTS_NAME = '//a[@class="name__comment__login--3E4k1"]'
    COMMENTS_BODY = '//div[@class="name__comment__content--3-Ipy"]'
    COMMENT = '//div[@class ="name__comments__underground--Zy1hx"]'
    ERROR_EMPTY = '//div[@class="name__error--FQ9hR"]'

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

    def set_comment(self, comment):
        self.driver.find_element_by_xpath(self.COMMENT_AREA).send_keys(comment)

    def submit_comment(self):
        self.driver.find_element_by_xpath(self.SUBMIT_COMMENT).click()

    def create_comment(self, comment):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.COMMENT_AREA)))
        self.set_comment(comment)
        self.submit_comment()

    def wait_comment(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.COMMENTS_NAME)))

    def get_count_comments(self):
        self.wait_comment()
        try:
            elements = self.driver.find_elements_by_xpath(self.COMMENTS_NAME)
            n = len(elements)
        except NoSuchElementException:
            return 0
        else:
            return n

    def check_new_comment(self, count, user, body):
        count = self.get_count_comments()
        locator = (By.XPATH, self.COMMENTS_NAME)
        WebDriverWait(self.driver, 4).until(customEC(locator, count))
        try:
            elements = self.driver.find_elements_by_xpath(self.COMMENTS_NAME)
            n = len(elements)
            username = elements[n-1].text
            elements = self.driver.find_elements_by_xpath(self.COMMENTS_BODY)
            n = len(elements)
            comment_body = elements[n-1].text
            print(user, '-', username, '\n', body, '-', comment_body)
        except NoSuchElementException:
            return False
        else:
            if username == user and comment_body.strip() == body:
                return True
            else:
                return False

    def check_empty_comment(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ERROR_EMPTY)))

