import os
import unittest
import codecs
import random
import config

from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from CalendarPage import CalendarPage

class CalendarTest(unittest.TestCase):
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome(config.DRIVER)
        self.editing = CalendarPage(self.driver)
        self.editing.sign_in(self.login, self.password)
        self.editing.open_sidebar()

    def tearDown(self):
        self.driver.quit()

    def test_adding_newCalendar(self):
        
        nameForForm = self.editing.create_newCalendar()
        newNames = self.editing.check_CalendarNames()
        self.assertTrue(nameForForm.decode("utf-8") in newNames)
  


    def test_editing_newCalendar(self):
        self.editing.create_newCalendar()
        
        nameForForm = self.editing.check_lastCalendarName()
        # print('\nnameForForm ' + nameForForm + ' \n')
        nameForm = "QWQ" + nameForForm
        
        self.editing.wait_redirect('https://m.calendar.mail.ru/')
        self.driver.refresh()
        self.editing.open_sidebar()
        self.editing.open_editCalendars()
        self.editing.openEdit_lastCalendar_inEditCalendars()
        self.editing.enter_nameOfNewCalendar(nameForm)
        self.editing.click_btnUpdateForms()
        
        nameForForm = nameForForm + nameForm
        # print('\ntest_editing_newCalendar ' + nameForForm + ' \n')
        self.assertTrue(self.editing.is_calendar_in_calendarsList(nameForForm))
        
    def test_delete_newCalendar(self):        
        nameForForm = self.editing.create_newCalendar()
        
        self.driver.refresh()
        self.editing.open_sidebar()
        
        calendar = self.editing.check_lastCalendarName()
        self.editing.open_editCalendars()
        self.editing.delete_lastCalendar_inEditCalendars()
        self.editing.close_editWindow()
        # print("test_delete_newCalendar assertFalse")
        self.assertFalse(self.editing.is_calendar_in_calendarsList(calendar))
        
     
    def test_delete_allCalendars(self):        
        self.editing.create_newCalendar()
        
        self.driver.refresh()
        self.editing.open_sidebar()
        
        calendars = self.editing.check_CalendarNames()
        self.editing.open_editCalendars()
        for i in range(len(calendars)):
            self.editing.delete_lastCalendar_inEditCalendars()
            
        self.editing.close_editWindow()
        
        calendars = self.editing.check_CalendarNames()
        
        self.assertEqual(len(calendars), 0)