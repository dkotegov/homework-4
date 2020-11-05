from pages.default import Page, Component


class TagPage(Page):
    PATH = 'page/sources'

    @property
    def form(self):
        return TagForm(self.driver)


class TagForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    DELETE = '//div[contains(@onclick, "deleteSourceFunc")]'
    IMG = '//img[contains(@id, "res_listSourceImage")][@src!="/cleverMan.jpg"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def delete_click(self):
        self.wait_for_visible(self.DELETE)
        self.driver.find_element_by_xpath(self.DELETE).click()

    def image_presents(self, value):
        self.wait_for_visible(self.IMG)
        return self.driver.find_element_by_xpath(self.IMG).get_attribute("src")
