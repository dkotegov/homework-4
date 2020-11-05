from base_classes.component import Component
from selenium.webdriver.common.keys import Keys


class CreateLabelPopup(Component):
    CONTAINER = '//div[contains(@class, "form pop-over")]'
    CREATE_LABEL_BUTTON = '//div[contains(@class, "js-createLabel")]'
    LABEL_NAME_INPUT = '//input[contains(@class, "js-inputLabelTitle")]'

    def set_label_name(self, name):
        self.driver.find_element_by_xpath(self.LABEL_NAME_INPUT).send_keys(name)

    def click_create_label_button(self):
        self.driver.find_element_by_xpath(self.CREATE_LABEL_BUTTON).click()
