import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


from margarita import utils
from margarita.pages.todo.default import Page


class MainPage(Page):
    TASK_INPUT =  'input.c0147[placeholder=\"Создать задачу\"]'
    TASKS = '//li[@class="BaseListMain_item__1UDQu"]'
    CREATED_TASK = '//p[contains(text(), "{}")]'

    DELETE_BUTTON = '//p[contains(text(), "Удалить")]'
    TASK_CHECKBOX_BY_CONTENT = '//p[contains(text(), "{}")]/parent::*/parent::*/parent::*//div[@class = "Task_checkbox__1kBaq"]'
    DONE_CHECKBOX = '//div[@class="c0168 c0172"]'

    def create_task(self, task_content):
        utils.wait_for_element_by_selector(self.driver, self.TASK_INPUT).send_keys(task_content + Keys.ENTER)
        utils.wait_for_element_to_be_clickable_by_xpath(self.driver, self.CREATED_TASK.format(task_content))

    def count_tasks(self):
        return len(self.driver.find_elements_by_xpath(self.TASKS))

    def mark_as_done(self, task_content):
        utils.wait_for_element_to_be_clickable_by_xpath(self.driver, self.TASK_CHECKBOX_BY_CONTENT.format(task_content)).click()

    def mark_undone(self):
        utils.wait_for_element_by_selector(self.driver, self.DONE_CHECKBOX).click()