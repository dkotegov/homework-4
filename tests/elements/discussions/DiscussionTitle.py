from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class DiscussionTitle(BaseElement):
    def get(self,title):
        return (By.XPATH, "//div[@class=disc-i_cnt_group_theme,text()="+title+"]")