from library.selenium import Component


class RepostForm(Component):
    REPOST_BUTTON = '//button[@class="h-mod widget_cnt"]'
    REPOST_SUBMIT = '//a[@class="u-menu_li js-doNotHide"]'

    def click(self):
        self.driver.find_element_by_xpath(self.REPOST_BUTTON).click()
        return self

    def submit(self):
        self.driver.find_element_by_xpath(self.REPOST_SUBMIT).click()
        return self
