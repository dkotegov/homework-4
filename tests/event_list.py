# -*- coding: utf-8 -*-
from tests.auth_page import authenticate
from utils import Page, Component, Test, wait_for_element_load
from selenium.webdriver.common.by import By


class EventListPage(Page):
    PATH = 'blog/view/33/'

    @property
    def event(self):
        return Event(self.driver)

class Event(Component):
    HEADER_PATH = '//h1[@class="topic-title"]/a'
    SUBHEADER_PATH = '//a[@class="topic-blog"]'
    SUBMIT_BUTTON_PATH = '//button[text()="Регистрация закрыта"]'

    def open_event(self):
        self._wait_for_xpath(self.HEADER_PATH)
        self.driver.find_element_by_xpath(self.HEADER_PATH).click()

    def open_blog(self):
        self._wait_for_xpath(self.SUBHEADER_PATH)
        self.driver.find_element_by_xpath(self.SUBHEADER_PATH).click()

    def participate(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).click()

    def get_button_text(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).text

    def get_button_color(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).value_of_css_property('background-color')

class EventListTest(Test):

    def test(self):
        authenticate(self.driver)
        self.event_list_page = EventListPage(self.driver)
        self.event_list_page.open()
        wait_for_element_load(self.driver, (By.XPATH, '//h2[@class="page-header"][text()="Мероприятия"]'))
