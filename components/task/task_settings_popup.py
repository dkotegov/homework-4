from base_classes.component import Component
from components.task.add_label_to_task_popup import AddLabelToTaskPopup
from components.task.create_label_popup import CreateLabelPopup
from components.task.create_checklist_popup import CreateChecklistPopup
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class TaskSettingsPopup(Component):
    CONTAINER = '//div[@class="task"]'
    DELETE_BUTTON = '//div[contains(@class, "js-deleteTask")]'
    TASK_NAME_TEXT_FIELD = '//input[contains(@class, "js-inputTitle")]'
    TASK_DESCRIPTION_TEXT_FIELD = '//div[contains(@class, "js-inputDescription")]'
    SAVE_DESCRIPTION_BUTTON = '//div[contains(@class, "js-saveTaskDescription")]'
    ADD_NEW_LABEL_BUTTON = '//div[contains(@class, "js-addNewLabel")]'
    CLOSE_POPUP_BUTTON = '//*[contains(@class, "js-closeTaskButton")]'
    ADD_NEW_CHECKLIST_BUTTON = '//*[contains(@class, "js-addNewChecklist")]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.add_label_to_task_popup = AddLabelToTaskPopup(self.driver)
        self.create_label_popup = CreateLabelPopup(self.driver)
        self.create_checklist_popup = CreateChecklistPopup(self.driver)

    def create_new_label_with_name(self, name):
        assert(self.is_open)

        self.add_label_to_task_popup.wait_for_container()
        self.add_label_to_task_popup.click_create_new_label_button()

        self.create_label_popup.wait_for_container()
        self.create_label_popup.set_label_name(name)
        self.create_label_popup.click_create_label_button()

    def add_label_with_name_to_task(self, label_name):
        assert(self.is_open)
        self.add_label_to_task_popup.wait_for_container()
        self.add_label_to_task_popup.click_create_new_label_button()

        self.create_label_popup.wait_for_container()
        self.create_label_popup.set_label_name(label_name)
        self.create_label_popup.click_create_label_button()

        self.add_label_to_task_popup.wait_for_container()
        self.add_label_to_task_popup.click_label_with_provided_name(label_name)

    def is_label_with_provided_name_exist(self, name):
        assert(self.is_open)
        self.click_add_new_label_button()
        self.add_label_to_task_popup.wait_for_container()
        return self.add_label_to_task_popup.is_label_with_provided_name_exist(name)

    def is_label_with_provided_name_bind_to_task(self, label_name):
        assert(self.is_open)
        label = f'//*[contains(@class, "task-label-list") and text()="{label_name}"]'

        try:
            self.driver.find_element_by_xpath(label)
        except:
            return False
        return True

    def is_checklist_with_provided_name_exist(self, checklist_name):
        assert(self.is_open)
        checklist = f'//*[contains(@class, "checklist-title") and text()="{checklist_name}"]'

        try:
            self.driver.find_element_by_xpath(checklist)
        except:
            return False
        return True

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

    def create_new_checklist_with_name(self, name: str):
        self.driver.find_element_by_xpath(self.ADD_NEW_CHECKLIST_BUTTON).click()
        self.create_checklist_popup.set_checklist_name(name)
        self.create_checklist_popup.click_create_checklist_button()

    def delete_task(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()

    def click_add_new_label_button(self):
        self.driver.find_element_by_xpath(self.ADD_NEW_LABEL_BUTTON).click()

    def close_add_labels_popup(self):
        assert(self.add_label_to_task_popup.is_open)
        self.add_label_to_task_popup.close_popup()

    def close_popup(self):
        assert(self.is_open)
        ActionChains(self.driver).click(
            self.driver.find_element_by_xpath(self.CLOSE_POPUP_BUTTON)
        )
