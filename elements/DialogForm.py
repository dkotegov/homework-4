# -*- coding: utf-8 -*-

from Component import Component
from selenium.webdriver.support.ui import WebDriverWait

class DialogForm(Component):
    DIALOGS_AVATAR = '(//img[@class="talk__user-image"])[1]'

    def get_dialogs_avatar_src(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIALOGS_AVATAR).get_attribute("src")
        )

    def go_to_user_page(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIALOGS_AVATAR)
        )
        link.click()
