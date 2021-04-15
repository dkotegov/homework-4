from selenium.webdriver.common.by import By

from testutils import Component
from .taskPriorityMenu import TaskPriorityMenu


class ContextMenu(Component):
    container = '[class^="ContextMenu_base"]'

    class Selectors:
        date_button = '[class^="MenuButton_base"]:nth-child(1)'
        for_task_list_delete_button = date_button
        priority_button = '[class^="MenuButton_base"]:nth-child(2)'
        delete_button = '[class^="MenuButton_base"]:nth-child(4)'

    def __press_button(self, selector):
        button_selector = self.container + ' ' + selector
        self._wait_visible(By.CSS_SELECTOR, button_selector)
        self._wait_clickable(By.CSS_SELECTOR, button_selector)
        self.driver.find_element_by_css_selector(button_selector).click()

    def delete_task_list(self):
        self.__press_button(self.Selectors.for_task_list_delete_button)

    def open_date_menu(self):
        self.__press_button(self.Selectors.date_button)

    def open_priority_menu(self) -> TaskPriorityMenu:
        self.__press_button(self.Selectors.priority_button)
        return TaskPriorityMenu(self.driver)

    def delete(self):
        self.driver.find_element_by_css_selector(self.container). \
            find_element_by_css_selector(self.Selectors.priority_button).click()