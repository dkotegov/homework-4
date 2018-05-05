# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support.ui import WebDriverWait

import time


class GroupTopMenu(Component):
    # Попроще сделать в формат
    THEMES_BUTTON = u'//div[@class="mctc_navMenu __groups"]/a[contains(text(),"Темы")]'
    LENTA_BUTTON = u'//div[contains(@class,"mctc_navMenu")]/a[contains(text(),"Лента")]'

    def themes_page_open(self):
        themes_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.THEMES_BUTTON)
        )
        themes_button.click()

    def lenta_page_open(self):
        # Надо придумать что с этим делать
        time.sleep(2)
        lenta_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LENTA_BUTTON)
        )
        lenta_button.click()


class GroupLeftMenu(Component):
    DELETE_BUTTON = u'//a[span[contains(text(),"Удалить")]]'
    OTHER_ACTION_BUTTON = u'//span[span[em[contains(text(),"Другие действия")]]]'
    CONFIRM_DELETE_BUTTON = u'//input[@name="button_delete"]'

    def delete_group(self):
        (WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OTHER_ACTION_BUTTON)
        )).click()

        themes_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUTTON)
        )
        themes_button.click()

        confirm_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_DELETE_BUTTON)
        )
        confirm_button.click()