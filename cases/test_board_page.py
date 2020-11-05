import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

from components.board.tasks.task import Task
from pages.board_page import BoardPage
from pages.boards_page import BoardsPage
from pages.login_page import LoginPage


class BoardPageTest(unittest.TestCase):
    BOARD_TITLE = 'TEST BOARD NAME'
    COLUMN_TITLE = 'TEST COLUMN'
    COLUMN_TITLE_2 = 'TEST COLUMN 2'
    TASK_TITLE = 'TEST_TASK'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

        self.login_page = LoginPage(self.driver)
        self.login_page.open()

        login = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')
        self.login_page.login(login, password)

        self.boards_page = BoardsPage(self.driver)
        self.boards_page.wait_for_container()
        self.boards_page.create_board(self.BOARD_TITLE)

        self.board_page = BoardPage(self.driver)
        self.board_page.wait_for_container()

    def tearDown(self):
        self.boards_page.open()
        self.boards_page.wait_for_container()

        self.boards_page.boards_list.open_board(self.BOARD_TITLE)
        self.board_page.wait_for_container()

        self.board_page.header.open_settings()
        self.board_page.settings_popup.delete_board()
        self.boards_page.wait_for_container()

        self.driver.quit()

    def test_open_settings_popup(self):
        self.board_page.header.open_settings()
        self.board_page.settings_popup.wait_for_container()

        self.assertTrue(self.board_page.settings_popup.is_open)

    def test_open_add_members_popup(self):
        self.board_page.header.open_add_members()
        self.board_page.settings_popup.wait_for_container()

        self.assertTrue(self.board_page.settings_popup.is_open)

    def test_create_column_success(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        self.assertIsNotNone(column)
        self.assertEqual(self.COLUMN_TITLE, column.get_title())

    def test_create_column_with_empty_title(self):
        create_column_form = self.board_page.columns_list.create_column_form
        create_column_form.open()
        create_column_form.set_title('')
        create_column_form.submit()

        with self.assertRaises(TimeoutException):
            create_column_form.wait_for_closed()

    def test_create_column_cancel(self):
        create_column_form = self.board_page.columns_list.create_column_form
        create_column_form.open()
        create_column_form.set_title(self.COLUMN_TITLE)
        create_column_form.close()
        create_column_form.wait_for_closed()

        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)
        self.assertIsNone(column)

    def test_column_change_title(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        new_title = 'MY NEW COLUMN'
        column.set_title(new_title)

        self.driver.refresh()
        self.board_page.wait_for_container()

        self.assertEqual(new_title, column.get_title())

    def test_column_name_change_title_to_empty(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        column.set_title('')

        self.driver.refresh()
        self.board_page.wait_for_container()

        self.assertNotEqual('', column.get_title())

    def test_column_delete(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        column.delete()
        self.driver.refresh()

        self.assertTrue(
            self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE) is None
        )

    def test_add_task(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        column.task_list.create_task(self.TASK_TITLE)
        task = column.task_list.get_task_by_title(self.TASK_TITLE)

        self.assertIsNotNone(task)
        self.assertEqual(self.TASK_TITLE, task.get_title())

    def test_add_task_with_empty_title(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        create_task_form = column.task_list.create_task_form
        create_task_form.open()
        create_task_form.set_title('')
        create_task_form.submit()

        with self.assertRaises(TimeoutException):
            create_task_form.wait_for_closed()

    def test_add_task_cancel(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        create_task_form = column.task_list.create_task_form
        create_task_form.open()
        create_task_form.set_title(self.TASK_TITLE)
        create_task_form.close()
        create_task_form.wait_for_closed()

        self.assertIsNone(column.task_list.get_task_by_title(self.TASK_TITLE))

    def test_create_task(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        column.task_list.create_task(self.TASK_TITLE)
        task = column.task_list.get_task_by_title(self.TASK_TITLE)

        self.assertIsNotNone(task)
        self.assertEqual(self.TASK_TITLE, task.get_title())

    def test_move_task_success(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column_from = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        self.board_page.columns_list.create_column(self.COLUMN_TITLE_2)
        column_to = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE_2)

        column_from.task_list.create_task(self.TASK_TITLE)
        task = column_from.task_list.get_task_by_title(self.TASK_TITLE)

        task_element = self.driver.find_element_by_xpath(task.CONTAINER)
        column_to_element = self.driver.find_element_by_xpath(column_to.CONTAINER)
        ActionChains(self.driver).drag_and_drop(task_element, column_to_element).perform()

        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(Task.create_xpath(column_to.column_id, task.task_id))
        )

        moved_task = column_to.task_list.get_task_by_title(self.TASK_TITLE)

        self.assertIsNotNone(moved_task)
        self.assertEqual(self.TASK_TITLE, moved_task.get_title())

    def test_move_task_fail(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column_from = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        self.board_page.columns_list.create_column(self.COLUMN_TITLE_2)
        column_to = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE_2)

        column_from.task_list.create_task(self.TASK_TITLE)
        task = column_from.task_list.get_task_by_title(self.TASK_TITLE)

        task_element = self.driver.find_element_by_xpath(task.CONTAINER)
        column_to_element = self.driver.find_element_by_xpath(self.board_page.main_header.NOTIFICATIONS_BUTTON)
        ActionChains(self.driver).drag_and_drop(task_element, column_to_element).perform()

        self.driver.refresh()

        unmoved_task = column_from.task_list.get_task_by_title(self.TASK_TITLE)

        self.assertIsNotNone(unmoved_task)
        self.assertEqual(self.TASK_TITLE, unmoved_task.get_title())
