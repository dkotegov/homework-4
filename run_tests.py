# -*- coding: utf-8 -*-

import os
import unittest
from datetime import datetime
from locale import setlocale, LC_TIME

from steps.auth import *
from steps.calendar import *


class TestClass(unittest.TestCase):
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
        login(self)

    def tearDown(self):
        self.driver.quit()

    # Создается событие с другими участниками.
    def test_create_event_w_attendees(self):
        result = set_create_event_w_attendees(self)
        self.assertTrue(result)

    # Создается событие длительностью более дня
    def test_create_event_2_day_duration(self):
        result = set_create_event_2_day_duration(self)
        self.assertTrue(result)

    # Создается события с указанием названия
    def test_mcreate_event_w_name(self):
        result = set_create_event_w_name(self)
        self.assertTrue(result)

    # Создается события с указанием места
    def test_create_event_w_location(self):
        result = set_create_event_w_location(self)
        self.assertTrue(result)

    # Создается события с указанием описания
    def test_create_event_w_description(self):
        result = set_create_event_w_description(self)
        self.assertTrue(result)

    # # Сохраняются нестандартные настройки напоминаний для новых событий. URL:https://calendar.mail.ru/ Ошибка:http://jira.bmstu.cloud/browse/QA-277
    # Хм. Трудновато проверить т.к. надо найти созданное событие на всей сетке

    # # Может быть выслано напоминание о событии по почте не меньше чем за минуту до самого события. URL:https://calendar.mail.ru/ Ошибка:http://jira.bmstu.cloud/browse/QA-280
    # Странный кейс. Напоминание МОЖЕТ быть выслано в тот же момент, что и событие

    # При выборе начала и конца рабочего дня настройки успешно сохраняются.
    def test_workday_times(self):
        result = set_workday_times(self)
        self.assertTrue(result)

    # При выборе основного календаря настройки успешно сохраняются.
    def test_main_calendar(self):
        result = set_main_calendar(self)
        self.assertTrue(result)

    # При выборе хотя бы двух рабочих дней настройки успешно сохраняются.
    def test_two_workdays(self):
        result = set_two_workdays(self)
        self.assertTrue(result)

    # При выборе ни одного рабочего дня настройки не сохраняются.
    def test_zero_workdays(self):
        result = set_zero_workdays(self)
        self.assertFalse(result)

    # Настройки успешно сохраняются при разрешении хотя бы одного способа напоминания о событии.
    def test_one_reminder(self):
        result = set_one_reminder(self)
        self.assertTrue(result)

    # Настройки успешно сохраняются при запрете всех способов напоминания о событии.
    def test_zero_reminders(self):
        result = set_zero_reminders(self)
        self.assertTrue(result)

    # Успешное сохранение настроек при отключении всех звуков в браузере.
    def test_mute_sound(self):
        result = set_sound_muted(self)
        self.assertTrue(result)

    # Успешное сохранение настроек при отметке всех вариантов получения уведомлений по электронной почте.
    def test_all_email_reminders(self):
        result = set_all_email_reminders(self)
        self.assertTrue(result)

    # Успешное сохранение настроек при выборе ни одного варианта уведомления по электронной почте.
    def test_zero_email_reminders(self):
        result = set_zero_email_reminders(self)
        self.assertTrue(result)

    # Добавление задачи без указания даты
    def test_task_add(self):
        task_topic = 'TASK_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        task_list_title = 'Неразобранное'
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))

    # Добавить задачу без указания даты и выполнить ее
    def test_task_execution(self):
        task_topic = 'TASK_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)
        execute_last_created_task_without_date(self)

        self.assertTrue(check_is_last_created_task_without_date_executed(self))

    # Добавить задачу и изменить дату
    def test_task_date_changing(self):
        task_topic = 'TASK_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        # change last created task's date to tomorrow
        tomorrow = datetime.datetime.today() + timedelta(days=1)
        set_date_last_created_task_without_date(self, tomorrow)

        task_list_title = 'Завтра'
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))

        task_topic = 'TASK_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_task_without_date(self, task_topic)

        # change last created task's date to some other date
        task_date = datetime.datetime.today() + timedelta(days=2)
        set_date_last_created_task_without_date(self, task_date)

        setlocale(LC_TIME, 'ru_RU.utf8')
        task_list_title = task_date.strftime("%d %B")
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))

    # Добавить задачу с указанием даты
    def test_task_with_date_creation(self):
        task_topic = 'TASK_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_date = datetime.datetime.today() + timedelta(days=1)

        create_task(self, task_topic, task_date)

        task_list_title = "Завтра"
        self.assertTrue(check_last_created_task_has_title(self, task_list_title, task_topic))


if __name__ == '__main__':
    unittest.main()
