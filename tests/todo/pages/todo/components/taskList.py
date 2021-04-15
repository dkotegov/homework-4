from selenium.webdriver.common.by import By
from .task import Task
from .TaskListSettings import TaskListSettings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import time

from testutils import Component


class TaskList(Component):

    class Selectors:
        title = '[placeholder="Добавить название"]'
        description = '[placeholder="Добавить описание"]'
        create_task = '[placeholder="Создать задачу"]'
        settings_button = 'button[class^="ASettingsButton_base"]'

    @property
    def settings(self) -> TaskListSettings:
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.settings_button)
        self.driver.find_element_by_css_selector(self.Selectors.settings_button).click()
        return TaskListSettings(self.driver)

    def get_task(self, title) -> Task:
        return Task(self.driver,
                    self._wait_visible(By.XPATH, Task.Selectors.task_by_name(title)))

    def create_task(self, title):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.create_task, title, True)
        self._wait_visible(By.XPATH, Task.Selectors.task_by_name(title))

    def wait_until_first_task_be(self, first_task_name, timeout=10, delay=0.1):
        start = time.time()
        while time.time() - start < timeout:
            if self.get_tasks()[0].get_text() == first_task_name:
                return
            time.sleep(delay)
        raise TimeoutError

    def get_tasks(self):
        self._wait_visible(By.CSS_SELECTOR, Task.container)
        self._dis_wait_visible(By.CSS_SELECTOR, '[data-task-id^="_"]')
        self._wait_visible(By.CSS_SELECTOR, Task.container)
        tasks = []
        for task in self.driver.find_elements(By.CSS_SELECTOR, Task.container):
            tasks.append(Task(self.driver, task))
        return tasks

    def wait_description(self, title):
        self._wait_text(By.CSS_SELECTOR, self.Selectors.description, title)

    def wait_title(self, title):
        self._wait_text(By.CSS_SELECTOR, self.Selectors.title, title)

    def wait_until_disappear_title(self, title):
        self._dis_wait_text(By.CSS_SELECTOR, self.Selectors.title, title)

    def wait_task_list(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.title)

    def fill_description(self, content):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.description, content, True)

    def clear_description(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.description, True)

    def get_description(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.description)
        return self.driver.find_element_by_css_selector(self.Selectors.description).text

    def rename_title(self, content):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.title, content, True)

    def fill_title(self, content):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.title, content, True)

    def clear_title(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title, True)

    def get_title(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.title)
        return self.driver.find_element_by_css_selector(self.Selectors.title).text
