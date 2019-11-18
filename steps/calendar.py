# coding=utf-8
from datetime import timedelta

from selenium.common.exceptions import NoSuchElementException

from pages.calendar import *


def set_create_event_w_attendees(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.add_attendees("iergeoi@e.mail.ru")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_create_event_2_day_duration(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    date = calendar.get_date_end()
    calendar.set_date_end(date + timedelta(days=2))
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_create_event_w_name(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_name("test name")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_create_event_w_location(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_location("test location")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_create_event_w_description(self):
    calendar = CalendarPage(self.driver).form
    calendar.create_event()
    calendar.set_description("test description")
    calendar.save_event()
    calendar.wait_for_disappear(calendar.EVENT_PAGE)
    try:
        calendar.driver.find_element_by_xpath(calendar.EVENT_PAGE)
    except NoSuchElementException:
        return True
    return False


def set_workday_times(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_workday_times()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_main_calendar(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_calendar()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_two_workdays(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_to_two_workdays()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_workdays(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.change_to_zero_workdays()
    calendar.settings_submit()

    try:
        calendar.driver.find_element_by_xpath(calendar.WORKDAY_CHECKBOX_ERROR)
    except NoSuchElementException:
        return True

    return False


def set_one_reminder(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_to_one_reminder()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_reminders(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_to_zero_reminders()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_sound_muted(self):
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.mute_sound()
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_all_email_reminders(self):
    select_all_state = 'true'
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_email_reminders(select_all_state)
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


def set_zero_email_reminders(self):
    select_all_state = 'false'
    calendar = CalendarPage(self.driver).form
    calendar.settings_click()
    calendar.reminders_click()
    calendar.change_email_reminders(select_all_state)
    calendar.settings_submit()
    calendar.wait_for_disappear(calendar.SETTINGS)

    try:
        calendar.driver.find_element_by_xpath(calendar.SETTINGS)
    except NoSuchElementException:
        return True

    return False


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
