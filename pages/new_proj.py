from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default import Page, Component, wait_for_the_attribute_value


class NewProjPage(Page):
    PATH = 'page/newproject'
    HEADER = '//h2[contains(text(), "Добавление проекта")]'

    @property
    def form(self):
        return NewProjForm(self.driver)


class NewProjForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    NAME = '//input[@id="pNameField"]'
    DESCRIPTION = '//textarea[@id="pDescriptionField"]'
    CREATE = '//div[@id="projectAddBtn"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def set_name(self, name):
        self.wait_for_visible(self.NAME)
        input_key = self.driver.find_element_by_xpath(self.NAME)
        input_key.clear()
        input_key.send_keys(name)

    def set_description(self, desc):
        self.wait_for_visible(self.DESCRIPTION)
        input_key = self.driver.find_element_by_xpath(self.DESCRIPTION)
        input_key.clear()
        input_key.send_keys(desc)

    def submit(self):
        self.wait_for_visible(self.CREATE)
        self.driver.find_element_by_xpath(self.CREATE).click()


