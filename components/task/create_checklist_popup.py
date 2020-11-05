from base_classes.component import Component
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class CreateChecklistPopup(Component):
    CONTAINER = '//div[contains(@class, "js-createChecklist")]'
    CREATE_CHECKLIST_BUTTON = '//div[contains(@class, "js-createChecklist")]'
    CHECKLIST_NAME_INPUT = '//input[contains(@class, "js-inputChecklistName")]'

    def click_create_checklist_button(self):
        self.driver.find_element_by_xpath(self.CREATE_CHECKLIST_BUTTON).click()

    def set_checklist_name(self, name):
        self.driver.find_element_by_xpath(self.CHECKLIST_NAME_INPUT).send_keys(name)
