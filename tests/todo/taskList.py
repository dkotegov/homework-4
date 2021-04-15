import uuid

from .utils import TodoTest


class TaskListTest(TodoTest):

    def test_change_description(self):
        description_content = 'Some description'
        task_list = self.page.task_list
        task_list.fill_description(description_content)
        self.driver.refresh()
        self.control_bar.wait_self()
        self.control_bar.open_task_list(self.task_list_title)
        task_list.wait_description(description_content)
        self.assertEqual(description_content, task_list.get_description())

    def test_change_title(self):
        title_content = 'Some title'
        task_list = self.page.task_list
        task_list.rename_title(title_content)
        self.task_list_title = title_content
        self.driver.refresh()
        self.control_bar.wait_self()
        self.control_bar.open_task_list(self.task_list_title)
        task_list.wait_title(title_content)
        self.assertEqual(title_content, task_list.get_title())

    def test_hide_completed(self):
        task_list = self.page.task_list
        task_list.create_task("Not hidden")
        task_list.create_task("Will hidden")

        task = task_list.get_task("Will hidden")
        task.toggle()

        settings = task_list.settings
        settings.wait_self()
        settings.hide_completed()

        tasks = task_list.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].get_text(), "Not hidden")

    def __bug_here_test_tasks_for_today(self):
        """По этому тесту найден баг в продукте, связанный с тем, что из списка 'на сегодня' не удаляются задачи при
        удалении их дочерних листов, после чего их нельзя ни удалить ни изменить"""
        task_list = self.page.task_list
        task_list.create_task("task in first list 1")
        task_list.create_task("task in first list 2")
        tasks = task_list.get_tasks()
        for task in tasks:
            task.set_date()

        new_task_list = uuid.uuid4().hex[:5]
        self.additional_task_lists.append(new_task_list)
        self.control_bar.create_list(new_task_list)
        self.control_bar.open_task_list(new_task_list)
        task_list.wait_title(new_task_list)
        task_list.create_task("task in second list 1")
        task_list.get_tasks()[0].set_date()

        self.driver.get(self.page.base_url + '/today')
        tasks = task_list.get_tasks()
        self.assertEqual(len(tasks), 3)

