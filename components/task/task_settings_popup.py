from base_classes.component import Component
from selenium.webdriver.common.keys import Keys

class TaskSettingsPopup(Component):
    CONTAINER = '//div[@class="task"]'
    DELETE_BUTTON = '//div[contains(@class, "js-deleteTask")]'
    TASK_NAME_TEXT_FIELD = '//input[contains(@class, "js-inputTitle")]'
    TASK_DESCRIPTION_TEXT_FIELD = '//div[contains(@class, "js-inputDescription")]'
    SAVE_DESCRIPTION_BUTTON = '//div[contains(@class, "js-saveTaskDescription")]'

    def get_task_name(self):
        return self.driver.find_element_by_xpath(self.TASK_NAME_TEXT_FIELD).get_attribute('value')

    def get_task_description(self):
        return self.driver.find_element_by_xpath(self.TASK_DESCRIPTION_TEXT_FIELD).text

    def rename_task(self, new_name: str):
        self.driver.find_element_by_xpath(self.TASK_NAME_TEXT_FIELD).clear()
        self.driver.find_element_by_xpath(self.TASK_NAME_TEXT_FIELD).send_keys(new_name, Keys.ENTER)

    def change_description(self, description: str):
        self.driver.find_element_by_xpath(self.TASK_DESCRIPTION_TEXT_FIELD).clear()
        self.driver.find_element_by_xpath(self.TASK_DESCRIPTION_TEXT_FIELD).send_keys(description)
        self.driver.find_element_by_xpath(self.SAVE_DESCRIPTION_BUTTON).click()

    def delete_task(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()