# -*- coding: utf-8 -*-
import datetime
import os
import unittest
from datetime import datetime, timedelta
from locale import setlocale, LC_TIME

from selenium import webdriver

from steps.auth import login
from steps.calendar import create_task_without_date, \
    execute_last_created_task_without_date, check_is_last_created_task_without_date_executed, \
    set_date_last_created_task_without_date, create_task, check_last_created_task_has_title


class TaskAddTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login(self)

        task_topic = 'TASK_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        task_list_title = 'Неразобранное'
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))


class TaskExecuteTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login(self)

        task_topic = 'TASK_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)
        execute_last_created_task_without_date(self)

        self.assertTrue(check_is_last_created_task_without_date_executed(self))


class TaskChangeDateTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )

    #
    def tearDown(self):
        self.driver.quit()

    def test(self):
        login(self)

        task_topic = 'TASK_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        # change last created task's date to tomorrow
        tomorrow = datetime.today() + timedelta(days=1)
        set_date_last_created_task_without_date(self, tomorrow)

        task_list_title = 'Завтра'
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))

        task_topic = 'TASK_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        # change last created task's date to some other date
        task_date = datetime.today() + timedelta(days=2)
        set_date_last_created_task_without_date(self, task_date)

        setlocale(LC_TIME, 'ru_RU.utf8')
        task_list_title = task_date.strftime("%d %B")
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))


class TaskCreateWithDateTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser_name = os.environ['BROWSER']
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                "browserName": browser_name,
            }
        )

    #
    def tearDown(self):
        self.driver.quit()

    def test(self):
        login(self)

        task_topic = 'TASK_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_date = datetime.today() + timedelta(days=1)

        create_task(self, task_topic, task_date)

        task_list_title = "Завтра"
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))
