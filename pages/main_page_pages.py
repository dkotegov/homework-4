# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class HeadMailPage:
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

    def get_text_login_incorrect(self):
        message = self.driver.find_elements_by_css_selector("div.x-ph__form__message:nth-child(2)")[0]
        return message.text

    def get_color_text_login_incorrect(self):
        element = self.driver.find_elements_by_css_selector("div.x-ph__form__message:nth-child(2)")[0]
        return element.value_of_css_property("color")

    def get_email_user_login_correct(self):
        return self.driver.find_element_by_id("PH_user-email").text

    def click_link(self, index):
        link = self.driver.find_elements_by_class_name("x-ph__link")[index]
        link.click()

    def click_link_registration(self):
        link = self.driver.find_element_by_id("PH_regLink")
        link.click()

class PortalMenuToolbarPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = ".js-link.pm-toolbar__button__inner.pm-toolbar__button__inner_noicon"
        self.logo = ".pm-logo__link"

    def move_to_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(link).perform()

    def get_background_color_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        return link.value_of_css_property("background-color")

    def click_logo(self):
        link = self.driver.find_elements_by_css_selector(self.logo)[0]
        link.click()

class PortalMenuSubmenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = "span.js-button:nth-child(5)"
        self.dropdown = "span.js-button:nth-child(5) > span:nth-child(2)"

    def move_to_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(link).perform()

    def get_dropdown(self):
        return self.driver.find_elements_by_css_selector(self.dropdown)[0]

    def dropdown_is_open(self):
        dropdown = self.get_dropdown()
        opacity = dropdown.value_of_css_property("opacity")
        visibility = dropdown.value_of_css_property("visibility")
        display = dropdown.value_of_css_property("display")
        print opacity,visibility,display

        if opacity == "1" and visibility == "visible" and display == "block":
            return True
        return False




class AdvertisingUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.links = ["div.item_small:nth-child(2)","div.item:nth-child(1)","#canvas",
                      "td.yap-layout__item:nth-child(1) > yatag:nth-child(1) > yatag:nth-child(1) > yatag:nth-child(2) > yatag:nth-child(1) > yatag:nth-child(1) > a:nth-child(1)",
                      "td.yap-layout__item:nth-child(2) > yatag:nth-child(1) > yatag:nth-child(1) > yatag:nth-child(2) > yatag:nth-child(1) > yatag:nth-child(1) > a:nth-child(1)",
                      "td.yap-layout__item:nth-child(3) > yatag:nth-child(1) > yatag:nth-child(1) > yatag:nth-child(2) > yatag:nth-child(1) > yatag:nth-child(1) > a:nth-child(1)"]

    def click_link(self, selector):
        link = self.driver.find_elements_by_css_selector(selector)[0]
        link.click()

class BlockHoroPage:
    def __init__(self, driver):
        self.driver = driver
        self.date_block = ".p-prediction__date__text"
        self.title = "h1.hdr__inner"

    def get_date(self):
        element = self.driver.find_elements_by_css_selector(self.date_block)[0]
        return element.text

    def get_horo_title(self):
        element = self.driver.find_elements_by_css_selector(self.title)[0]
        return element.text

    def click_button_choice_date(self, index):
        selector = "a.filter__item_white:nth-child(" + str(index) + ")"
        link = self.driver.find_elements_by_css_selector(selector)[0]
        link.click()

