from pages.default import Page, Component


class IframePage(Page):
    PATH = 'page/iframe'

    @property
    def form(self):
        return IframeForm(self.driver)


class IframeForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    GENERATE = '//div[@id="getIframeBtn"]'
    RESULT = '//div[@id="elementBoxOfContent"]//textarea'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def generate_click(self):
        self.wait_for_visible(self.GENERATE)
        self.driver.find_element_by_xpath(self.GENERATE).click()

    def iframe_presents(self):
        self.wait_for_visible(self.RESULT)
        return self.driver.find_element_by_xpath(self.RESULT).\
            get_attribute("innerHTML")
