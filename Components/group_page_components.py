# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support.ui import WebDriverWait


class Popup(Component):
    CREATE_GROUP = '//div[@class="create-group"]//a'
    CREATE_SHOP = '//a[contains(@href,"SHOP")]'

    SHOP_NAME = '//input[@id="field_name"]'
    GAMES_SUBCATEGORY = '//select[@id="field_pageMixedCategory"]/option[@value="subcatVal12006"]'
    SUBMIT = '//input[@id="hook_FormButton_button_create"]'

    def open_popup(self):
        create_groups_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_GROUP)
        )
        create_groups_button.click()

    def create_shop(self):
        create_shop_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_SHOP)
        )
        create_shop_button.click()

    def set_shop_name(self, shop_name):
        shop_name_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SHOP_NAME)
        )
        shop_name_input.send_keys(shop_name)

    def set_subcategory(self):
        games_option = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.GAMES_SUBCATEGORY)
        )
        games_option.click()

    def submit_creation(self):
        submit_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        submit_button.click()