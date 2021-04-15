from datetime import datetime

from .utils import TodoTest


class TaskTest(TodoTest):
    def test_create_task(self):
        task_name = 'Some task name'
        task_list = self.page.task_list
        task_list.create_task(task_name)
        tasks = task_list.get_tasks()
        task = tasks[0]

        self.assertEqual(task_name, task.get_text())

    def test_toggle_task(self):
        task_name = 'Some task name'
        task_list = self.page.task_list
        task_list.create_task(task_name)
        task = task_list.get_tasks()[0]
        task.toggle()

        self.assertTrue(task.is_checked())

    def test_set_priority(self):
        task_name = 'Some task name'
        task_list = self.page.task_list
        task_list.create_task(task_name)
        task = task_list.get_tasks()[0]
        priority = 'medium'
        task.set_priority(priority)

        self.assertEqual(priority, task.get_priority())

    def test_change_task(self):
        task_name = 'New task change'
        new_task_name = 'Changed task name'

        task_list = self.page.task_list
        task_list.create_task(task_name)
        task = task_list.get_tasks()[0]

        self.assertEqual(task_name, task.get_text())

        task.rename_task(new_task_name)
        self.driver.refresh()
        task = task_list.get_tasks()[0]

        self.assertEqual(new_task_name, task.get_text())

    def test_set_date(self):
        task_name = 'Some task name'
        task_list = self.page.task_list
        task_list.create_task(task_name)
        task = task_list.get_tasks()[0]
        today = datetime.now()
        task.set_date()
        date = task.get_date()

        self.assertTrue(f'{today.day}' in date)
