from steps.default import DefaultSteps
from pages.head import HeadPage

import time

class Head(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = HeadPage(driver)

    def click_logo(self):
        self.page.open()
        self.page.click_on_close_notion()
        self.page.click_on_logo()

    def click_help(self):
        self.page.open()
        self.page.click_on_close_notion()
        self.page.click_on_help()
