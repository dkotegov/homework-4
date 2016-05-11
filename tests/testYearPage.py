# -*- coding: utf-8 -*-
import os

import unittest
import urlparse
import time


from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date

class Page(object):
    BASE_URL = 'https://calendar.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)



class Component(object):
    def __init__(self, driver):
        self.driver = driver

class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//button[text()="Войти"]'
    YEAR_BUTTON = '//span[@name="year"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def year(self):
        self.driver.find_element_by_xpath(self.YEAR_BUTTON).click()

class YearNav(Page):
    @property
    def nav(self):
        return Nav(self.driver)

class Nav(Component):
    YEAR_CAPTION = '//div[@class="year-caption"]'
    PREV_BUTTON = '//a[@class="button button_color_dark grid-prev"]'
    NEXT_BUTTON = '//a[@class="button button_color_dark grid-next"]'

    def prev_period(self):
        self.driver.find_element_by_xpath(self.PREV_BUTTON).click()

    def next_period(self):
        self.driver.find_element_by_xpath(self.NEXT_BUTTON).click()

    def get_year(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.YEAR_CAPTION).text
        )

class Calendar_table(Page):
    @property
    def table(self):
        return year_table(self.driver)

class year_table(Component):
    DAY_BUTTON = '//a[@data-day="12"]'
    WEEK_TABLE = '//div[@class="weekTmp"]'

    def select_day(self):
        self.driver.find_element_by_xpath(self.DAY_BUTTON).click()
    def test_week(self):
        try:
            self.driver.find_element_by_xpath(self.WEEK_TABLE)
            return True
        except NoSuchElementException:
            return False

class Preferences(Page):
    @property
    def pref(self):
        return side_bar(self.driver)

class side_bar(Component):
    OPEN_BUTTON = '//div[@class="preferences__button button button_color_dark"]'
    PREF_OPEN = '//div[@class="preferences preferences_open"]'
    CHECK_CALENDARS = '//span[text()="Календари"]'
    CHECK_TODO = '//span[text()="Дела"]'
    CHECK_WEEKNUMBER = '//span[text()="Нижний календарь"]'
    CALENDARS_OPEN = '//div[@class="preferences preferences_open"]'
    CALENDARS_CLOSE = '//div[@class="sidebar sidebar_left sidebar_collapsed"]'
    TODO_OPEN = '//div[@class="sidebar sidebar_right sidebar_right_expanded"]'
    TODO_CLOSE = '//div[@class="sidebar sidebar_right sidebar_right_collapsed"]'
    FLATCAL_OPEN = '//canvas[@class="flat-calendar__canvas"]'

    def test_click(self):
        self.driver.find_element_by_xpath(self.OPEN_BUTTON).click()

    def click_calend(self):
        self.driver.find_element_by_xpath(self.CHECK_CALENDARS).click()

    def click_todo(self):
        self.driver.find_element_by_xpath(self.CHECK_TODO).click()

    def click_flatcal(self):
        self.driver.find_element_by_xpath(self.CHECK_WEEKNUMBER).click()

    def test_open(self):
        try:
            self.driver.find_element_by_xpath(self.PREF_OPEN)
            return True
        except NoSuchElementException:
            return False

    def check_cal_open(self):
        try:
            self.driver.find_element_by_xpath(self.CALENDARS_OPEN)
            return True
        except NoSuchElementException:
            return False

    def check_cal_close(self):
        try:
            self.driver.find_element_by_xpath(self.CALENDARS_CLOSE)
            return True
        except NoSuchElementException:
            return False

    def check_todo_open(self):
        try:
            self.driver.find_element_by_xpath(self.TODO_OPEN)
            return True
        except NoSuchElementException:
            return False

    def check_todo_close(self):
        try:
            self.driver.find_element_by_xpath(self.TODO_CLOSE)
            return True
        except NoSuchElementException:
            return False

    def check_flatcal_open(self):
        try:
            self.driver.find_element_by_xpath(self.FLATCAL_OPEN)
            return True
        except NoSuchElementException:
            return False


class Tests(unittest.TestCase):
    USERNAME = u'Test1232323'
    PASSWORD = u'Qq654321'

    def setUp(self):

        self.driver = webdriver.Firefox()

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
        auth_form.year()



    def tearDown(self):
        self.driver.quit()

    def test_period_navigation(self):
        current_year = date.today().year
        year_nav = YearNav(self.driver)
        navigation = year_nav.nav
        self.assertEqual(str(current_year), navigation.get_year())

        navigation.prev_period()
        self.assertEqual(str(current_year - 1), navigation.get_year())

        navigation.next_period()
        self.assertEqual(str(current_year), navigation.get_year())

    def test_day(self):
        calendar_table = Calendar_table(self.driver)
        table = calendar_table.table
        table.select_day()
        self.assertEqual(True,table.test_week())

    def test_pref(self):
        pref_bar = Preferences(self.driver)
        bar = pref_bar.pref
        bar.test_click()
        self.assertEqual(True, bar.test_open())

        bar.click_calend()
        self.assertEqual(True, bar.check_cal_close())

        bar.click_calend()
        self.assertEqual(True, bar.check_cal_open())

        bar.click_todo()
        self.assertEqual(True, bar.check_todo_close())

        bar.click_todo()
        self.assertEqual(True, bar.check_todo_open())

        bar.click_flatcal()
        self.assertEqual(False, bar.check_flatcal_open())

        bar.click_flatcal()
        self.assertEqual(True, bar.check_flatcal_open())

        bar.test_click()
        self.assertEqual(False, bar.test_open())


