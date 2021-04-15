from .utils import TodoTest


class SortTest(TodoTest):
    def setUp(self):
        super().setUp()
        self.task_list = self.page.task_list
        self.task_list.create_task('task1')
        self.task_list.create_task('task2')
        self.task_list.create_task('task3')

    def test_sort_by_priority(self):
        tasks = self.task_list.get_tasks()

        tasks[0].set_priority('low')
        tasks[0].rename_task('low')

        tasks[1].set_priority('medium')
        tasks[1].rename_task('medium')

        tasks[2].set_priority('high')
        tasks[2].rename_task('high')

        self.task_list.settings.sort_by_priority()

        self.task_list.wait_until_first_task_be('high')

        tasks = self.task_list.get_tasks()

        self.assertEqual(tasks[0].get_text(), 'high')
        self.assertEqual(tasks[1].get_text(), 'medium')
        self.assertEqual(tasks[2].get_text(), 'low')

    def test_sort_by_name(self):
        tasks = self.task_list.get_tasks()

        tasks[0].rename_task('zoo')
        tasks[1].rename_task('guru')
        tasks[2].rename_task('alphabet')

        self.task_list.settings.sort_by_name()

        self.task_list.wait_until_first_task_be('alphabet')

        tasks = self.task_list.get_tasks()
        self.assertEqual(tasks[0].get_text(), 'alphabet')
        self.assertEqual(tasks[1].get_text(), 'guru')
        self.assertEqual(tasks[2].get_text(), 'zoo')

    def test_sort_by_date(self):
        tasks = self.task_list.get_tasks()

        tasks[0].rename_task('after tomorrow')
        tasks[0].set_date(2)

        tasks[1].rename_task('tomorrow')
        tasks[1].set_date(1)

        tasks[2].rename_task('today')
        tasks[2].set_date()

        self.task_list.settings.sort_by_date()

        self.task_list.wait_until_first_task_be('today')

        tasks = self.task_list.get_tasks()

        self.assertEqual(tasks[0].get_text(), 'today')
        self.assertEqual(tasks[1].get_text(), 'tomorrow')
        self.assertEqual(tasks[2].get_text(), 'after tomorrow')
