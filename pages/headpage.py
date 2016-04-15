# -*- coding: utf-8 -*-
import unittest

class HeadPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        self.driver.find_element_by_id("PH_authLink").click()

        inputs = self.driver.find_elements_by_class_name("x-ph__form__input__text")
        inputs[0].send_keys(login)
        inputs[1].send_keys(password)

        self.driver.find_elements_by_class_name("x-ph__button__input")[0].click()

    def logout(self):
        button_logout = self.driver.find_element_by_id("PH_logoutLink")
        button_logout.click()

    def get_color_text_login_incorrect(self):
        message = self.driver.find_elements_by_css_selector("div.x-ph__form__message:nth-child(2)")[0]
        return message.text

    def get_text_login_incorrect(self):
        message = self.driver.find_elements_by_css_selector("div.x-ph__form__message:nth-child(2)")[0]
        return message.value_of_css_property("color")

    def get_email_user_login_correct(self):
        return self.driver.find_element_by_id("PH_user-email").text

    def clik_link(self, index):
        link = self.driver.find_elements_by_class_name("x-ph__link")[index]
        link.click()

    def click_link_registraition(self):
        link = self.driver.find_element_by_id("PH_regLink")
        link.click()