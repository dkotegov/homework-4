import os
import unittest

from selenium import webdriver
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
        self.board_page.header.open_settings()
        self.board_page.settings_popup.delete_board()
        self.boards_page.wait_for_container()

        self.driver.quit()

    def test_create_column_success(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        self.assertIsNotNone(column)
        self.assertEqual(self.COLUMN_TITLE, column.get_title())

    def test_create_task(self):
        self.board_page.columns_list.create_column(self.COLUMN_TITLE)
        column = self.board_page.columns_list.get_column_by_title(self.COLUMN_TITLE)

        column.task_list.create_task(self.TASK_TITLE)
        task = column.task_list.get_task_by_title(self.TASK_TITLE)

        self.assertIsNotNone(task)
        self.assertEqual(self.TASK_TITLE, task.get_title())

    def test_move_task(self):
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
