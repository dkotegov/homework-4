# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support.ui import WebDriverWait


class LeftMenu(Component):
    GROUPS_ITEM = '//a[contains(@href,"groups")]'

    def open_groups_page(self):
        groups_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.GROUPS_ITEM)
        )
        groups_button.click()
