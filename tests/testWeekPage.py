# -*- coding: utf-8 -*-

import os

import unittest
import urlparse
import datetime, time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys


def auth(driver):
    USEREMAIL = os.environ['HW4LOGIN']
    PASSWORD = os.environ['HW4PASSWORD']

    auth_page = AuthPage(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.set_login(USEREMAIL)
    auth_form.set_password(PASSWORD)
    auth_form.submit()

def week_calendar(driver):
    calendar_page = CalendarPage(driver)
    calendar_page.open()

    calendar_toolbar = calendar_page.toolbar
    calendar_toolbar.choise_week()

    return calendar_page

# ============================================= Pages ========================================

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

    @property
    def portal_headline(self):
        return PortalHeadline(self.driver)


class CalendarPage(Page):
    @property
    def toolbar(self):
        return CalendarToolbar(self.driver)

    @property
    def navigation_header(self):
        return NavigationHeaderToolbar(self.driver)

    @property
    def navigation_header_preferences(self):
        return NavigationHeaderPreferences(self.driver)

    @property
    def calendar_table(self):
        return CalendarTable(self.driver)

    @property
    def sidebar(self):
        return Sidebar(self.driver)



# ========================================== Components ======================================

class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = 'Login'
    PASSWORD = 'Password'
    SUBMIT = '//button[text()="Войти"]'

    def set_login(self, login):
        self.driver.find_element_by_name(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_name(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class PortalHeadline(Component):
    USERNAME = 'PH_user-email'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id(self.USERNAME).text
        )


class CalendarToolbar(Component):
    NAME = 'week'
    WEEK_NUMBER = 'week__caption-text_week-number'

    def choise_week(self):
        self.driver.find_element_by_name(self.NAME).click()

    def get_week_number(self):
        self.driver.execute_script( "document.getElementsByClassName('"+self.WEEK_NUMBER+"')[0].style.display = 'block';")
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name(self.WEEK_NUMBER).text
        )


class NavigationHeaderToolbar(Component):
    NEXT = 'grid-next'
    PREV = 'grid-prev'
    TODAY = 'month-day_today'

    def next_week(self):
        self.driver.find_element_by_class_name(self.NEXT).click()

    def prev_week(self):
        self.driver.find_element_by_class_name(self.PREV).click()

    def check_today(self):
        try:
            self.driver.find_element_by_class_name(self.TODAY)
            return True
        except NoSuchElementException, e:
            return False


class NavigationHeaderPreferences(Component):
    CLASS_NAME = 'preferences__button'
    OPEN_PREFERENCES_CLASS_NAME = 'preferences_open'

    def open(self):
        self.driver.find_element_by_class_name(self.CLASS_NAME).click()

    def close(self):
        if self.check_open():
            self.driver.find_element_by_class_name(self.CLASS_NAME).click()

    def check_open(self):
        try:
            self.driver.find_element_by_class_name(self.OPEN_PREFERENCES_CLASS_NAME)
            return True
        except NoSuchElementException, e:
            return False


class CalendarTable(Component):
    TODAY = 'week__grid__day_today'

    def open_new_event(self):
        self.driver.find_element_by_class_name(self.TODAY).click()

    def set_title(self, title):
        title_elem = self.driver.find_elements_by_css_selector('.textbox-control__input.textbox_default__input')[1]
        title_elem.send_keys(title)

    def add_friend(self, friend_email):
        friend = self.driver.find_elements_by_css_selector('.js-input.compose__labels__input')[0]
        friend.send_keys(friend_email)

    def extra_options(self, description):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Больше параметров')]")[0].click()
        self.driver.find_element_by_css_selector('.textbox__textarea.textarea').send_keys(description)

    def check_description(self, description):
        self.driver.find_elements_by_xpath("//*[contains(text(), '" + description + "')]")[0].text

    def submit(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Сохранить')]")[1].click()
        # time.sleep(5)

    def check_event(self, title):
        timeout = 20
        counter = 0

        # fucking awesome code:
        # because ajax-query: visible - true, clickable - not true => Zzzz
        while True:
            try:
                self.driver.find_elements_by_xpath("//*[contains(text(), '" + title + "')]")[0].click()
                _timeout = 20
                _counter = 0
                while True:
                    if self.check_event_info():
                        break
                    else:
                        _counter += 1
                        time.sleep(0.5)

                    if _counter == _timeout:
                        return False

                return True
            except WebDriverException, e:
                pass
            except IndexError, e:
                pass

            counter += 1
            time.sleep(0.5)

            if counter == timeout:
                return False

    def check_event_info(self):
        if len(self.driver.find_elements_by_class_name("event-info__summary")) == 0:
            return False
        else:
            return True

    def check_edit_btn(self):
        if len(self.driver.find_elements_by_xpath("//*[contains(text(), 'Редактировать')]")) == 0:
            return False
        else:
            return True

    def check_title(self, title):
        self.driver.find_elements_by_xpath("//*[contains(text(), '" + title + "')]")[0].text

    def check_friend_name(self):
        friend_name = self.driver.find_element_by_css_selector('.attendees-list__item.attendees-list__item_needs-action').text
        return friend_name

    def del_event(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Удалить')]")[0].click()
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Да')]")[0].click()

    def click_edit(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Редактировать')]")[0].click()


class Sidebar(Component):

    def set_task_name(self, text):
        self.driver.find_elements_by_css_selector('.textbox-control__input.textbox_default__input')[0].send_keys(text)

    def add_task(self, text):
        self.set_task_name(text)
        self.driver.find_elements_by_css_selector('.textbox-control__input.textbox_default__input')[0].send_keys(Keys.RETURN)

    def del_task(self, text):
        self.driver.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")[0].click()
        time.sleep(1)	# ajax here

    def check_task(self, text):
        try:
            self.driver.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")[0]
            return True
        except NoSuchElementException, e:
            return False
        except IndexError, e:
            return False

    def hover(self, title):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath(
            '//*[@title="' + title + '"]'
        ))
        action.perform()
        time.sleep(2)

    def edit_task(self):
        self.hover("Редактировать задачу")
        self.driver.find_elements_by_xpath('//*[@title="Редактировать задачу"]')[0].click()
        # self.driver.find_elements_by_xpath("//*[contains(text(), 'Редактировать задачу')]")[0].click()
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Сохранить')]")[1].click()

    def del_button_task(self):
        self.hover("Редактировать задачу")
        self.driver.find_elements_by_xpath('//*[@title="Редактировать задачу"]')[0].click()
        # self.driver.find_elements_by_xpath("//*[contains(text(), 'Редактировать задачу')]")[0].click()
        self.driver.find_elements_by_xpath('//*[@title="Удалить задачу"]')[0].click()
        self.driver.find_elements_by_xpath('//*[contains(text(), "Да")]')[0].click()

    def extra_options_cancel(self):
        self.hover("Дополнительные параметры задачи")
        self.driver.find_elements_by_xpath('//*[@title="Дополнительные параметры задачи"]')[0].click()
        self.driver.find_elements_by_xpath('//*[contains(text(), "Отмена")]')[0].click()

    def extra_options_save(self):
        self.hover("Дополнительные параметры задачи")
        self.driver.find_elements_by_xpath('//*[@title="Дополнительные параметры задачи"]')[0].click()
        self.driver.find_elements_by_xpath('//*[contains(text(), "Сохранить")]')[0].click()


class Tests(unittest.TestCase):
    USEREMAIL = os.environ['HW4LOGIN']
    PASSWORD = os.environ['HW4PASSWORD']


    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_week(self):
        calendar_page = CalendarPage(self.driver)
        calendar_page.open()

        calendar_toolbar = calendar_page.toolbar
        calendar_toolbar.choise_week()

        week_number = calendar_toolbar.get_week_number()

        true_week_number = datetime.datetime.now().strftime("%W")

        self.assertEqual(true_week_number, week_number)

    def test_navigation(self):
        calendar_page = CalendarPage(self.driver)
        header = calendar_page.navigation_header

        # Test next week
        header.next_week()
        calendar_toolbar = calendar_page.toolbar
        time.sleep(1)
        week_number = int(calendar_toolbar.get_week_number())
        true_week_number = int(datetime.datetime.now().strftime("%W")) + 1
        self.assertEqual(true_week_number, week_number)

        # Test true week
        header.prev_week()
        calendar_toolbar = calendar_page.toolbar
        time.sleep(1)
        week_number = calendar_toolbar.get_week_number()
        true_week_number = datetime.datetime.now().strftime("%W")
        self.assertEqual(true_week_number, week_number)

    def test_preferences(self):
        calendar_page = CalendarPage(self.driver)
        preferences = calendar_page.navigation_header_preferences

        # Open preferences
        preferences.open()
        check_open = preferences.check_open()
        self.assertEqual(True, check_open)

        # Close preferences
        preferences.close()
        check_close = preferences.check_open()
        self.assertEqual(False, check_close)

    TITLE = 'PYTHON DYE'
    NEW_TITLE = 'PYTHON BURN IN HELL'
    FRIEND_EMAIL = 'aaaaaaaaaaaaaa_aaaaaaaa_aaaaaaa@bk.ru'
    FRIEND_NAME = u'AAAAAAAAAAAAAA AAAAAAAAAAAAAA'
    DESCRIPTION = 'I HATE PYTHON'

    def test_add_event(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event()
        table.set_title(self.TITLE)
        table.add_friend(self.FRIEND_EMAIL)
        table.submit()

        check_event = table.check_event(self.TITLE)
        self.assertEqual(True, check_event)
        table.check_title(self.TITLE)

        check_friend_name = table.check_friend_name()
        self.assertEqual(self.FRIEND_NAME, check_friend_name)

        table.del_event()

    def test_add_event_with_extra_options(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event()
        table.set_title(self.TITLE)
        table.extra_options(self.DESCRIPTION)
        table.submit()

        # Like assert
        table.check_event(self.TITLE)
        table.check_title(self.TITLE)
        table.check_description(self.DESCRIPTION)

        table.del_event()

    def test_edit_event(self):
        calendar_page = CalendarPage(self.driver)
        table = calendar_page.calendar_table

        table.open_new_event()
        table.set_title(self.TITLE)
        table.add_friend(self.FRIEND_EMAIL)
        table.submit()

        table.check_event(self.TITLE)
        table.click_edit()
        table.set_title(self.NEW_TITLE)
        table.submit()

        # Like assert
        table.check_event(self.NEW_TITLE)
        table.check_title(self.NEW_TITLE)

        table.del_event()

    TEXT = 'HELLO'

    def test_task(self):
        calendar_page = CalendarPage(self.driver)
        sidebar = calendar_page.sidebar

        sidebar.add_task(self.TEXT)
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(True, check_task)

        sidebar.del_task(self.TEXT)
        self.driver.refresh()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(False, check_task)

    def test_edit_task(self):
        calendar_page = CalendarPage(self.driver)
        sidebar = calendar_page.sidebar

        sidebar.add_task(self.TEXT)

        sidebar.edit_task()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(True, check_task)

        sidebar.del_task(self.TEXT)

    def test_del_button_task(self):
        calendar_page = CalendarPage(self.driver)
        sidebar = calendar_page.sidebar

        sidebar.add_task(self.TEXT)

        sidebar.del_button_task()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(False, check_task)

    def test_cancel_button_task(self):
        calendar_page = CalendarPage(self.driver)
        sidebar = calendar_page.sidebar

        sidebar.set_task_name(self.TEXT)

        sidebar.extra_options_cancel()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(False, check_task)

    def test_save_button_task(self):
        calendar_page = CalendarPage(self.driver)
        sidebar = calendar_page.sidebar

        sidebar.set_task_name(self.TEXT)

        sidebar.extra_options_save()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(True, check_task)

        sidebar.del_task(self.TEXT)
        self.driver.refresh()
        check_task = sidebar.check_task(self.TEXT)
        self.assertEqual(False, check_task)