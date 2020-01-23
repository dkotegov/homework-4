# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage
from selenium.webdriver import ActionChains


class LetterReplier(BasicPage):

    reply_button = '.button2_reply'

    def __init__(self, driver):
        self.driver = driver

    def click_reply_button(self):
        elem = self.wait_render(self.reply_button)
        elem.click()
