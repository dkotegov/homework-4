from testutils import Page
from .components import Task, TaskList, ControlBar


class TodoPage(Page):
    base_url = 'https://todo.mail.ru'

    @property
    def task(self):
        return Task(self.driver)

    @property
    def control_bar(self):
        return ControlBar(self.driver)

    @property
    def task_list(self):
        return TaskList(self.driver)
