from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class DiscussionTitle(BaseElement):
    def get_by_title(self, title):
        self.locator = (By.XPATH, "//div[@class=disc-i_cnt_group_theme,text()=" + title + "]")
        return self
