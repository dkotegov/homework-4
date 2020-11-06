from base_classes.component import Component
from components.task.add_label_to_task_popup import AddLabelToTaskPopup
from components.task.create_label_popup import CreateLabelPopup
from components.task.create_checklist_popup import CreateChecklistPopup
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time


class TaskSettingsPopup(Component):
    CONTAINER = '//div[@class="task"]'
    DELETE_BUTTON = '//div[contains(@class, "js-deleteTask")]'
    TASK_NAME_TEXT_FIELD = '//input[contains(@class, "js-inputTitle")]'
    TASK_DESCRIPTION_TEXT_FIELD = '//div[contains(@class, "js-inputDescription")]'
    SAVE_DESCRIPTION_BUTTON = '//div[contains(@class, "js-saveTaskDescription")]'
    ADD_NEW_LABEL_BUTTON = '//div[contains(@class, "js-addNewLabel")]'
    CLOSE_POPUP_BUTTON = '//*[contains(@class, "js-closeTaskButton")]'
    ADD_NEW_CHECKLIST_BUTTON = '//div[contains(@class, "js-addNewChecklist")]'
    DELETE_CHECKLIST_BUTTON = '//div[contains(@class, "js-deleteChecklist")]'
    COMMENT_INPUT = '//div[contains(@class, "js-commentText")]'
    SAVE_COMMENT_BUTTON = '//div[contains(@class, "js-saveComment")]'
    ADD_NEW_ITEM_INTO_CHECKLIST_BUTTON = '//div[contains(@class, "js-addNewChecklistItem")]'
    NEW_ITEM_INPUT = '//input[contains(@class, "js-inputNewItemTitle")]'
    CREATE_CHECKLIST_ITEM_BUTTON = '//div[contains(@class, "js-createChecklistItem")]'
    CHECKLIST_ITEM_CHECKBOX = '//div[contains(@class, "custom-checkbox")]'
    CHECKLIST_PROGRESSBAR = '//div[contains(@class, "checklist-progressbar-progress")]'

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

    def add_item_into_checklist(self, name: str):
        self.driver.find_element_by_xpath(self.ADD_NEW_ITEM_INTO_CHECKLIST_BUTTON).click()
        self.driver.find_element_by_xpath(self.NEW_ITEM_INPUT).send_keys(name)
        self.driver.find_element_by_xpath(self.CREATE_CHECKLIST_ITEM_BUTTON).click()

    def is_checklist_item_with_provided_text_exist(self, text: str):
        assert(self.is_open)
        item_xpath = f'//div[contains(@class, "custom-label") and text()="{text}"]'

        try:
            self.driver.find_element_by_xpath(item_xpath)
        except:
            return False
        return True

    def click_on_item_checkbox(self):
        self.driver.find_element_by_xpath(self.CHECKLIST_ITEM_CHECKBOX).click()

    def is_item_in_checklist_marked(self):
        style = self.driver.find_element_by_xpath(self.CHECKLIST_PROGRESSBAR).get_attribute('style')
        return 'width: 0%' not in style

    def delete_task(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()

    def delete_checklist_with_name(self, name: str):
        assert(self.is_open)
        checklist_xpath = f'//*[contains(@class, "checklist-title") and text()="{name}"]'

        checklist = None
        try:
            checklist = self.driver.find_element_by_xpath(checklist_xpath)
        except:
            return

        delete_button = None
        try:
            delete_button = checklist.find_element_by_xpath(self.DELETE_CHECKLIST_BUTTON)
        except:
            return

        delete_button.click()

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

    def create_comment_with_text(self, text: str):
        assert(self.is_open)
        self.driver.find_element_by_xpath(self.COMMENT_INPUT).send_keys(text)
        self.driver.find_element_by_xpath(self.SAVE_COMMENT_BUTTON).click()

    def delete_comment(self):
        assert(self.is_open)
        comment_xpath = '//div[@class="task-settings-comment"]'
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(comment_xpath)
        ).perform()
        self.driver.find_element_by_xpath('//div[contains(@class, "js-deleteComment")]').click()

        def is_comment_div_dissapear(driver):
            try:
                driver.find_element_by_xpath(comment_xpath)
            except:
                return True
            return False

        WebDriverWait(self.driver, 3, 0.1).until(
            lambda d: is_comment_div_dissapear(self.driver)
        )

    def is_comment_with_provided_text_exist(self, text: str):
        assert(self.is_open)
        comment_xpath = f'//*[contains(@class, "task-settings-comment") and text()="{text}"]'
        try:
            self.driver.find_element_by_xpath(comment_xpath)
        except:
            return False
        return True
