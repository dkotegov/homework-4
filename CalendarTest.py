import os
import unittest
import random
import config
from CalendarPage import CalendarPage

from selenium import webdriver


class CalendarTest(unittest.TestCase):
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')
    BASE_URL = 'https://m.calendar.mail.ru/'
    CALENDAR_URL = 'https://m.calendar.mail.ru/calendar/new/'

    def setUp(self):
        self.driver = webdriver.Chrome(config.DRIVER)
        self.editing = CalendarPage(self.driver)
        self.editing.sign_in(self.login, self.password)
        self.editing.open_sidebar()

    def tearDown(self):
        self.driver.quit()

    def create_new_calendar(self, nameForForm=("rubbishName" + str(random.randrange(1, 30000)))):
        self.editing.open_addNewCalendar()
        self.editing.wait_redirect(self.CALENDAR_URL)
        self.editing.enter_calendar_name(nameForForm)
        self.editing.choose_calendar_color()
        self.editing.click_btn_update_forms()
        return nameForForm

    def test_adding_new_calendar(self):
        nameForForm = self.create_new_calendar()
        newNames = self.editing.check_calendar_names()
        self.assertTrue(nameForForm.decode("utf-8") in newNames)

    def test_editing_new_calendar(self):
        self.create_new_calendar()

        nameForForm = self.editing.check_last_calendar_name()
        nameForm = "QWQ" + nameForForm

        self.editing.wait_redirect(self.BASE_URL)
        self.driver.refresh()
        self.editing.open_sidebar()
        self.editing.open_edit_calendars()
        self.editing.edit_last_calendar()
        self.editing.enter_calendar_name(nameForm)
        self.editing.click_btn_update_forms()

        nameForForm = nameForForm + nameForm
        self.assertTrue(self.editing.in_calendar_list(nameForForm))

    def test_delete_new_calendar(self):
        self.driver.refresh()
        self.editing.open_sidebar()

        calendar = self.editing.check_last_calendar_name()
        self.editing.open_edit_calendars()
        self.editing.delete_last_calendar()
        self.editing.close_edit_window()
        self.assertFalse(self.editing.in_calendar_list(calendar))

    def test_delete_all_calendars(self):
        self.create_new_calendar()

        self.driver.refresh()
        self.editing.open_sidebar()

        calendars = self.editing.check_calendar_names()
        self.editing.open_edit_calendars()
        for _ in range(len(calendars)):
            self.editing.delete_last_calendar()

        self.editing.close_edit_window()
        calendars = self.editing.check_calendar_names()
        self.assertEqual(len(calendars), 0)
