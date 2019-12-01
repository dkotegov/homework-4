import os
import unittest
import random

from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.common.by import By

class CalendarPage:
    BASE_URL = 'https://m.calendar.mail.ru/login'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.BASE_URL)
    
        
    # Вход и вспомогательные функции
        
    def sign_in(self, login, password):

        def open():
            url = self.BASE_URL
            self.driver.get(url)
            self.wait_redirect(url)
            self.driver.maximize_window()

        def enter_login(login):
            elem = self.wait_renderbtn('input[name=Login]')
            elem.send_keys(login)

        def enter_password(password):
            elem = self.wait_renderbtn('input[name=Password]')
            elem.send_keys(password)

        def func_login():
            elem = self.wait_renderbtn('.login-button')
            elem.click()
        
        open()
        enter_login(login)
        enter_password(password)
        func_login()
        self.wait_redirect('https://m.calendar.mail.ru/', 10)
        
    def create_newCalendar(self, nameForForm = ("rubbishName" + str(random.randrange(1, 30000)))):
        self.open_addNewCalendar()
        self.wait_redirect('https://m.calendar.mail.ru/calendar/new/');
        self.enter_nameOfNewCalendar(nameForForm)
        self.choose_randomColor_inNewCalendar()
        self.click_btnUpdateForms()
        
        return nameForForm

    def wait_redirect(self, url, timeout = 15):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
    
    def wait_renderbtn(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    
    def wait_presenceLocated(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
    def wait_invisible(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def open_sidebar(self):
        login_but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.header-menu-item.header-menu-item__sidebutton.header-menu-item__list')))
        login_but.click()
    
    def click_btnUpdateForms(self):
        elem = self.wait_renderbtn('div.header-menu-item.header-menu-item__sidebutton.header-menu-item__ok')
        elem.click()

    def is_calendar_in_calendarsList(self, calendar):
        self.driver.refresh()
        self.open_sidebar() 
        calendars = self.check_CalendarNames()
        # print(calendar.encode('ascii', 'ignore'))
        # print(calendars)
        return (calendar.encode('ascii', 'ignore') in calendars)
         

    # Добавление календаря

    def open_addNewCalendar(self):
        login_but = self.wait_renderbtn('.calendar-create-item.panel-item.panel-item__marked')
        self.driver.execute_script("arguments[0].click();", login_but)
        element = self.wait_renderbtn('.calendar-create-item.panel-item.panel-item__marked')
        ActionChains(self.driver).move_to_element(element ).click(element ).perform()
        
    def close_sidebar(self):
        elem = self.wait_renderbtn('div.header-menu-item.header-menu-item__sidebutton.header-menu-item__forward')
        elem.click()
        
    def enter_nameOfNewCalendar(self, name):
        elem = self.wait_renderbtn('input.panel-input__white.calendar-summary-input')
        elem.send_keys(name)
        
    def choose_randomColor_inNewCalendar(self):
        toColors = self.wait_renderbtn('div.panel-item.calendar-color-chooser.panel-item__last')
        toColors.click()
        
        number_of_color_in_que = 2
        elem = self.wait_renderbtn('div.panel-item.panel-item__withcols.color-item:nth-child(%s)' % (number_of_color_in_que))
        elem.click()
        
    def check_CalendarNames(self):
        self.driver.refresh()
        self.open_sidebar()

        elem = self.wait_renderbtn('.panel-content.panel-content__dark:not(.settings-panel)')
        options = [(x.text) for x in elem.find_elements_by_css_selector("div.panel-item-text.panel-item-text__nowrap")]
        return options
    
    def check_lastCalendarName(self):
        self.wait_renderbtn('.panel-content.panel-content__dark:not(.settings-panel)')
        elem = self.wait_renderbtn('.panel-content.panel-content__dark:not(.settings-panel) .panel-item:first-child')

        return (elem.text)
        
    # Редактирование календаря
    
    def open_editCalendars(self):
        elem = self.wait_presenceLocated('div.calendars-edit.panel-item.panel-item__marked.panel-item__last')
        elem = self.wait_invisible('div.calendars-edit.panel-item.panel-item__marked.panel-item__last')

        webdriver.ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        
    def delete_lastCalendar_inEditCalendars(self):
        self.wait_presenceLocated('.panel-content.panel-content__dark .panel-item:first-child .icn__calendar.icn__calendar-delete').click()
        self.wait_presenceLocated('div.button.button-delete.button__big').click()
    
    def openEdit_lastCalendar_inEditCalendars(self):
        elem = self.wait_renderbtn('.panel-content.panel-content__dark .panel-item:first-child .icn__calendar.icn__calendar-settings')
        elem.click()
        
    def addRubbish_inEditCalendars(self):
        elem = self.wait_renderbtn('input.panel-input__white.calendar-summary-input')
        elem.send_keys("addRubbish")
    
    def close_editWindow(self):
        self.wait_renderbtn('div.header-menu-item.header-menu-item__sidebutton.header-menu-item__close').click()
        
    