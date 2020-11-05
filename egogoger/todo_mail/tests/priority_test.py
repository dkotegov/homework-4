import os

from egogoger.todo_mail.pages.main_page import MainPage
from egogoger.todo_mail.pages.auth_page import AuthPage
from egogoger.base_test import Test
from egogoger.utils import set_input
from .auth_test import auth_test


class PriorityTest(Test):
    TODO_NAMES = ["First", "Second", "Third"]

    def setUp(self):
        auth_test(self)
        # Create 3 new todos
        main_page = MainPage(self.driver)
        main_page.delete_todos(self)
        for iii in range(len(self.TODO_NAMES)):
            main_page.create_todo(self.TODO_NAMES[iii], iii)
        self.driver.get(self.driver.current_url)
        main_page.check_for_self(self)

    def tearDown(self):
        # Delete all todos
        MainPage(self.driver).delete_todos(self)

    def test_priority_click(self):
        main_page = MainPage(self.driver)
        main_page.open_todo_options(0, self)
        main_page.open_priority_list()
        main_page.check_priority_list_open(self)

    def test_set_priority(self):
        main_page = MainPage(self.driver)

        for priority in main_page.PRIORITY_NAMES:
            main_page.set_priority(0, priority, self)
            main_page.check_priority(0, priority, self)
            main_page.choose_priority(priority) # just ot exit window
    
    def test_priority_order(self):
        main_page = MainPage(self.driver)

        # Change priorities
        main_page.set_priority(0, main_page.HIGH_PRIORITY, self)
        main_page.set_priority(1, main_page.MID_PRIORITY, self)
        main_page.set_priority(2, main_page.LOW_PRIORITY, self)

        # Sort
        main_page.set_sort(main_page.SORT_BY_PRIORITY)

        # Check
        main_page.check_todo_order(self)
