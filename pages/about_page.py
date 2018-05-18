import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import constants
from components.base_component import BaseComponent
from components.about_form import AboutForm
from components.page import Page
from constants import profiles


class AboutPage(Page):

    def __init__(self, driver, url):
        super(AboutPage, self).__init__(driver)
        self.about_form = AboutForm(self.driver)
        self.PAGE = url + "/about"

    def add_to_reletionship(self, name):
        self.about_form.marital_status_specify().click()
        self.about_form.rilationship().click()
        self.about_form.search_friend().send_keys(name)
        self.about_form.add_rilationship().click()

    def break_reletionship(self):
        self.about_form.rilationship().click()
        self.about_form.break_rilationship().click()

