# coding=utf-8
from pages.calendar import *


def create_task(self, task_topic, date):
    task_date_formatted = date.strftime("%Y-%m-%dT00:00:00+03:00")
    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks

    tasks_wrapper.set_task_title(task_topic)
    tasks_wrapper.open_task_settings()
    tasks_wrapper.set_task_date(task_date_formatted)
    tasks_wrapper.add_task_with_date()


def create_task_without_date(self, task_topic):
    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks

    tasks_wrapper.set_task_title(task_topic)
    tasks_wrapper.add_task()


def check_last_created_task_has_title(self, task_list_title, task_title):
    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks
    return tasks_wrapper.is_task_has_title(task_list_title, task_title)


def execute_last_created_task_without_date(self):
    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks
    task_list_title = "Неразобранное"

    tasks_wrapper.execute_task(task_list_title)


def check_is_last_created_task_without_date_executed(self):
    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks
    task_list_title = "Неразобранное"

    return tasks_wrapper.is_last_created_task_crossed(task_list_title)


def set_date_last_created_task_without_date(self, date):
    task_date_formatted = date.strftime("%Y-%m-%dT00:00:00+03:00")

    cal_page = CalendarPage(self.driver)
    tasks_wrapper = cal_page.tasks
    task_list_title = "Неразобранное"

    tasks_wrapper.open_last_created_task_settings(task_list_title)
    tasks_wrapper.set_task_date(task_date_formatted)
    tasks_wrapper.save_task_settings()


def open_profile_settings_page(self):
    cal_page = CalendarPage(self.driver)
    settings_wrapper = cal_page.settings()

    settings_wrapper.open_settings()
    settings_wrapper.open_notifications_tab()
    settings_wrapper.add_phone_number()
