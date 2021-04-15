import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Remote, ActionChains
from selenium.common.exceptions import TimeoutException

from testutils import Component
from .taskPriorityMenu import TaskPriorityMenu
from .contextMenu import ContextMenu
from .DatePicker import DatePicker


class Task(Component):
    container = '[class^="BaseListMain_item"]'

    class Selectors:
        text = '[class^="Task_text"] [class^="EditableText"] p'
        text_input = '[class^="Task_text"]'  # [class^="EditableText"] p'
        checkbox = '[class^="TaskCheckbox"] label'
        date_picker = 'div[class^="Task_datepicker"] button'
        date_picker_date = 'div[class^="Task_datepicker"] u'
        priority_button = '[class^="Task_priority"] [class^="PickerButton_base"]'
        task_id_selector = lambda task_id: f'[data-task-id="{task_id}"] [class^="Task_base"]'
        task_by_name = lambda name: f'//div[starts-with(@class, "Task_base")]' \
                                    f'//div[starts-with(@class, "Task_text")]' \
                                    f'//p[text()="{name}"]/../../../../..'

    def __init__(self, driver: Remote, element: WebElement):
        super().__init__(driver)
        self.element_selector = self.get_element_selector(element.get_attribute('data-task-id'))

    @property
    def element(self):
        return self.driver.find_element_by_css_selector(self.element_selector)

    def get_element_selector(self, task_id):
        return self.Selectors.task_id_selector(task_id)

    def is_checked(self) -> bool:
        selector = self.element_selector + ' ' + self.Selectors.text_input + ' ' + 's'
        try:
            self._wait_visible(By.CSS_SELECTOR, selector)
        except TimeoutException:
            return False
        return True

    def rename_task(self, name):
        self._wait_visible(By.CSS_SELECTOR, self.element_selector)
        selector = self.element_selector + ' ' + self.Selectors.text_input
        self._wait_visible(By.CSS_SELECTOR, selector)
        self.hover()
        self._wait_clickable(By.CSS_SELECTOR, selector)
        self.driver.find_element_by_css_selector(selector).click()
        selector += ' [class^="MultilineInput"]'
        self._wait_visible(By.CSS_SELECTOR, selector)
        text = self._find(selector).text
        self._fill_input(By.CSS_SELECTOR, selector, Keys.BACKSPACE * len(text) + name, True, False)

    def get_text(self) -> str:
        return self.element.find_element_by_css_selector(self.Selectors.text).text

    def toggle(self):
        selector = self.element_selector + ' ' + self.Selectors.checkbox
        self._wait_visible(By.CSS_SELECTOR, selector)
        self._wait_clickable(By.CSS_SELECTOR, selector)
        self._find(selector).click()

    def open_date_picker(self):
        self._wait_visible(By.CSS_SELECTOR, self.element_selector)
        self.hover()
        selector = self.element_selector + ' ' + self.Selectors.date_picker
        self._wait_visible(By.CSS_SELECTOR, selector)
        self._wait_clickable(By.CSS_SELECTOR, selector)
        self._find(selector).click()
        return DatePicker(self.driver)

    def set_date(self, days_from_today=0):
        date_picker = self.open_date_picker()
        date_picker.choose_day(days_from_today)

    def get_date(self):
        element_date_selector = self.element_selector + ' ' + self.Selectors.date_picker_date
        self._wait_visible(By.CSS_SELECTOR, element_date_selector)
        return self._find(element_date_selector).text

    def get_priority(self) -> str:
        priority_level_selector = '[class*=Priority_level]'
        selector = self.element_selector + ' ' + priority_level_selector
        self._wait_visible(By.CSS_SELECTOR, selector)
        priority = self.driver.find_element_by_css_selector(selector)
        classname = priority.get_attribute('class')
        priority_classname = classname.split(' ')[1]
        level = int(priority_classname.split('_')[1][-1])
        if level == 1:
            return 'low'
        if level == 2:
            return 'medium'
        if level == 3:
            return 'high'

    def set_priority(self, priority):
        if priority == 'low':
            selector = TaskPriorityMenu.Selectors.low_priority
        elif priority == 'medium':
            selector = TaskPriorityMenu.Selectors.medium_priority
        elif priority == 'high':
            selector = TaskPriorityMenu.Selectors.high_priority
        else:
            selector = TaskPriorityMenu.Selectors.none_priority

        self.hover()
        self.open_priority_menu().choose_priority(selector)
        self.click()

    def click(self):
        self._wait_visible(By.CSS_SELECTOR, self.element_selector)
        self._wait_clickable(By.CSS_SELECTOR, self.element_selector)
        self._find(self.element_selector).click()

    def hover(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector(self.element_selector)
        ).perform()

    def open_priority_menu(self) -> TaskPriorityMenu:
        self._wait_clickable(By.CSS_SELECTOR, self.element_selector + ' ' + self.Selectors.priority_button)
        self.driver.find_element_by_css_selector(self.element_selector + ' ' + self.Selectors.priority_button).click()
        return TaskPriorityMenu(self.driver)

    def open_context_menu(self) -> ContextMenu:
        ActionChains(self.driver).context_click(self.element).perform()
        return ContextMenu(self.driver)

    def delete(self):
        context_menu = self.open_context_menu()
        context_menu.wait_self()
        context_menu.delete()
