from tests.components.component import Component

from selenium.webdriver.support.wait import WebDriverWait


class ManageTagsForm(Component):
    SELECT = '//input[@id="{}" and contains(@class, "change-rest-tags__checkbox")]'
    SUBMIT = '//button[@id="change-rest-tags__submit"]'
    MESSAGE = '//div[@class="message"]'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT).is_displayed()
        )

    def set_tag(self, tag_id):
        tag = self.driver.find_element_by_xpath(self.SELECT.format(tag_id))
        if not tag.is_selected() :
            tag.click()

    def unset_tag(self, tag_id):
        tag = self.driver.find_element_by_xpath(self.SELECT.format(tag_id))
        if tag.is_selected():
            tag.click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def message(self):
        return self.driver.find_element_by_xpath(self.MESSAGE).text
