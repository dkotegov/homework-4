from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os


class SearchPage(Page):
    PATH = '/search'
    SEARCH = '//input[@name="search"]'
    FILMS = '//span[@id="films"]'
    END = '//span[@id="endOfSearch"]'
    PEOPLE = '//span[@id="people"]'
    ACTORS = '//span[@id="actors"]'
    FILMS_LIST = '//div[@class="name__image__text--3JD50"]'
    ACTORS_LIST = '//div[@class="name__personLenta_image__text--DNHUk"]'
    USER = '//span[@class="name__profile__default_margin--_Vkp5 name__profile_login--2W71f"]'
    PEOPLE_LIST = '//a[@class="name__friendList_login--gKHhK"]'

    def fill_search(self, string):
        self.driver.find_element_by_xpath(self.SEARCH).send_keys(string)

    def get_search_value(self):
        return self.driver.find_element_by_xpath(self.SEARCH).get_attribute('value')

    def open_films(self):
        self.driver.find_element_by_xpath(self.FILMS).click()

    def open_people(self):
        self.driver.find_element_by_xpath(self.PEOPLE).click()

    def open_actors(self):
        self.driver.find_element_by_xpath(self.ACTORS).click()

    def get_films_list(self):
        return self.driver.find_elements_by_xpath(self.FILMS_LIST)

    def get_actors_list(self):
        return self.driver.find_elements_by_xpath(self.ACTORS_LIST)

    def get_people_list(self):
        return self.driver.find_elements_by_xpath(self.PEOPLE_LIST)

    def click_people(self):
        self.driver.find_element_by_xpath(self.PEOPLE_LIST).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USER)))

    def wait_for_end_of_search(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.END)))
