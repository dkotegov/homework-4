from selenium.webdriver.remote.webdriver import WebDriver

from base_classes.component import Component
from components.board.tasks.create_task_form import CreateTaskForm
from components.board.tasks.task import Task


class TasksList(Component):
    CONTAINER = '//div[@class="task-list"]'

    def __init__(self, driver: WebDriver, column_id: int, ):
        Component.__init__(self, driver)
        self.column_id = column_id
        self.CONTAINER = f'//div[@class="task-list" and @data-column-id="{column_id}"]'

    @property
    def create_task_form(self):
        return CreateTaskForm(self.driver, self.column_id)

    def create_task(self, title: str):
        self.create_task_form.open()
        self.create_task_form.set_title(title)
        self.create_task_form.submit()
        self.create_task_form.wait_for_closed()

    def get_task_by_title(self, title: str):
        tasks = self.driver.find_element_by_xpath(self.CONTAINER).find_elements_by_xpath(Task.CONTAINER)

        task_id = None
        for i in range(len(tasks)):
            raw_task = tasks[i]
            task_title = raw_task.find_element_by_xpath(Task.TITLE).text
            if task_title == title:
                task_id = int(raw_task.get_attribute('data-task-id'))
                break

        if task_id is None:
            return None

        return Task(self.driver, self.column_id, task_id)
