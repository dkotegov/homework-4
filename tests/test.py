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

'''
export HW4BROWSER=FIREFOX
export HW4LOGIN=HW4LOGIN_CALENDAR
export HW4PASSWORD=HW4PASSWORD_CALENDAR
'''

MONTHS = {
	'January': u'январь',
	'February': u'февраль',
	'March': u'март',
	'April': u'апрель',
	'May': u'май',	
	'June': u'июнь',
	'July': u'июль',
	'August': u'август',
	'September': u'сентябрь',
	'October': u'октябрь',
	'November': u'ноябрь',
	'December': u'декабрь',
}

def auth(driver):
	USEREMAIL = os.environ['HW4LOGIN']
	PASSWORD = os.environ['HW4PASSWORD']

	auth_page = AuthPage(driver)
	auth_page.open()

	auth_form = auth_page.form
	auth_form.set_login(USEREMAIL)
	auth_form.set_password(PASSWORD)
	auth_form.submit()

def month_calendar(driver):
	calendar_page = CalendarPage(driver)
	calendar_page.open()

	calendar_toolbar = calendar_page.toolbar
	calendar_toolbar.choise_month()

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
	NAME = 'month'
	MONTH_CLASS_NAME = 'month-caption'

	def choise_month(self):
		self.driver.find_element_by_name(self.NAME).click()

	def get_month_name(self):
		return WebDriverWait(self.driver, 30, 0.1).until(
			lambda d: d.find_element_by_class_name(self.MONTH_CLASS_NAME).text.split(',')[0].lower()	# because format like 'Month, year' e.g. 'Апрель, 2016'
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
	TODAY = 'month-day_today'
	
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
		timeout = 10
		counter = 0

		# because ajax-query: visible - true, clickable - not true => Zzzz 
		while True:
			try:
				self.driver.find_elements_by_xpath("//*[contains(text(), '" + title + "')]")[0].click()
				if self.check_edit_btn():
					return True
			except WebDriverException, e:
				pass
			
			counter += 1
			time.sleep(1)
			
			if counter == timeout:
				return False
	
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

		

# ============================================ Tests =========================================

class BaseClassTest(unittest.TestCase):

	def setUp(self):
		browser = os.environ.get('HW4BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		auth(self.driver)

	def tearDown(self):
		self.driver.quit()


class AuthTest(BaseClassTest):
	USERNAME = u'Александр Конышев'
	USEREMAIL = os.environ['HW4LOGIN']
	PASSWORD = os.environ['HW4PASSWORD']
	USER_EMAIL = 'hw4login_calendar@mail.ru'

	def setUp(self):
		browser = os.environ.get('HW4BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)



	def test_auth(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(self.USEREMAIL)
		auth_form.set_password(self.PASSWORD)
		auth_form.submit()

		user_email = auth_page.portal_headline.get_username()
		self.assertEqual(self.USER_EMAIL, user_email)


class MonthToolbarTest(BaseClassTest):

	def test_month(self):
		calendar_page = CalendarPage(self.driver)
		calendar_page.open()

		calendar_toolbar = calendar_page.toolbar
		calendar_toolbar.choise_month()

		month_name = calendar_toolbar.get_month_name()

		true_month_name = MONTHS[datetime.datetime.now().strftime("%B")]

		self.assertEqual(true_month_name, month_name)


class HeaderTest(BaseClassTest):
	NAVIGATION = 'month-day_today'

	def setUp(self):
		super(HeaderTest, self).setUp()
		self.calendar_page = month_calendar(self.driver)




	def test_navigation(self):
		header = self.calendar_page.navigation_header
		
		# Test next week
		header.next_week()
		today = header.check_today()
		self.assertEqual(False, today)

		# Test true week
		header.prev_week()
		today = header.check_today()
		self.assertEqual(True, today)
		# today = datetime.date.today()
		# next_month = MONTHS[datetime.datetime(today.year, today.month+1, 1).strftime("%B")]
		# self.assertEqual(next_month, month_name)

		# # Test true week
		# month_name = calendar_toolbar.get_month_name()
		# true_month_name = MONTHS[datetime.datetime.now().strftime("%B")]
		# self.assertEqual(true_month_name, month_name)


	def test_preferences(self):
		preferences = self.calendar_page.navigation_header_preferences

		# Open preferences
		preferences.open()
		check_open = preferences.check_open()
		self.assertEqual(True, check_open)

		# Close preferences
		preferences.close()
		check_close = preferences.check_open()
		self.assertEqual(False, check_close)


class CalendarTableTest(BaseClassTest):
	TITLE = 'TITLE'
	NEW_TITLE = 'HELLO'
	FRIEND_EMAIL = 'aaaaaaaaaaaaaa_aaaaaaaa_aaaaaaa@bk.ru'
	FRIEND_NAME = u'AAAAAAAAAAAAAA AAAAAAAAAAAAAA'
	DESCRIPTION = 'Blah-Blah-Blah'

	def setUp(self):
		super(CalendarTableTest, self).setUp()
		self.calendar_page = month_calendar(self.driver)

	def test_add_event(self):
		table = self.calendar_page.calendar_table

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
		table = self.calendar_page.calendar_table

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
		table = self.calendar_page.calendar_table

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


class SidebarTest(BaseClassTest):
	TEXT = 'HELLO'

	def setUp(self):
		super(SidebarTest, self).setUp()
		self.calendar_page = month_calendar(self.driver)
	
	def test_task(self):
		sidebar = self.calendar_page.sidebar

		sidebar.add_task(self.TEXT)
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(True, check_task)

		sidebar.del_task(self.TEXT)
		self.driver.refresh()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(False, check_task)

	def test_edit_task(self):
		sidebar = self.calendar_page.sidebar

		sidebar.add_task(self.TEXT)
		
		sidebar.edit_task()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(True, check_task)

		sidebar.del_task(self.TEXT)

	def test_del_button_task(self):
		sidebar = self.calendar_page.sidebar

		sidebar.add_task(self.TEXT)
		
		sidebar.del_button_task()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(False, check_task)

	def test_cancel_button_task(self):
		sidebar = self.calendar_page.sidebar

		sidebar.set_task_name(self.TEXT)
		
		sidebar.extra_options_cancel()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(False, check_task)

	def test_save_button_task(self):
		sidebar = self.calendar_page.sidebar

		sidebar.set_task_name(self.TEXT)
		
		sidebar.extra_options_save()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(True, check_task)

		sidebar.del_task(self.TEXT)
		self.driver.refresh()
		check_task = sidebar.check_task(self.TEXT)
		self.assertEqual(False, check_task)
