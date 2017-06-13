# -*- coding: utf-8 -*-

from Component import Component
from selenium.webdriver.support.ui import WebDriverWait

class UserForm(Component):
    USERNAME = '//h1[@class="profile__full-name"]'
    AVATAR = '//img[@class="profile__photo"]'

    def user_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )

    def get_avatar_src(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVATAR).get_attribute("src")
        )
