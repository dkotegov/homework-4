# -*- coding: utf-8 -*-

from Page import Page

class CreatePage(Page):
    PATH = '/talk/'
    MESSAGE = '//td[@class="cell-title talk__message"]'

    def message_open(self):
        self.driver.find_element_by_xpath(self.MESSAGE).click()