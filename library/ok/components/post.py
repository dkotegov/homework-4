from library.selenium import Component


class PostForm(Component):
    TEXT = '//div[@class="posting_itx emoji-tx h-mod js-ok-e ok-posting-handler"]'
    SUBMIT = '//div[@class="posting_submit button-pro"]'

    def add_text(self, text):
        self.driver.find_element_by_xpath(self.TEXT).send_keys(text)
        return self

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        return self

    def is_enabled(self):
        return len(self.driver.find_elements_by_xpath(self.SUBMIT)) > 0
