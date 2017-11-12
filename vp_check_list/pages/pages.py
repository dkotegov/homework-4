# -*- coding: utf-8 -*-
import os
import urlparse

from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
	BASE_URL = 'https://www.ok.ru'
	PATH = ''

	def __init__(self, driver):
		self.driver = driver

	def open(self):
		url = urlparse.urljoin(self.BASE_URL, self.PATH)
		self.driver.get(url)
		self.driver.maximize_window()


class Component(object):
	def __init__(self, driver):
		self.driver = driver


class AuthPage(Page):
	PATH = ''

	@property
	def form(self):
		return AuthForm(self.driver)

	@property
	def user_header(self):
		return UserHeader(self.driver)

	def login(self):
		user_login = 'technopark34'
		password = os.environ['OK_PASSWORD']

		auth_form = self.form
		auth_form.set_login(user_login)
		auth_form.set_password(password)
		auth_form.submit()

		return self.user_header.get_username()


class AuthForm(Component):
	LOGIN = '//input[@id="field_email"]'
	PASSWORD = '//input[@id="field_password"]'
	LOGIN_BUTTON = '//input[@class="button-pro __wide"]'

	def set_login(self, login):
		self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

	def set_password(self, pwd):
		self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

	def submit(self):
		self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()


class UserHeader(Component):
	USERNAME = '//h1[@class="mctc_name_tx bl"]'

	def get_username(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.USERNAME).text
		)


class UserPage(Page):
	PATH = ''

	def login(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		return auth_page.login()

	@property
	def post(self):
		return UserPost(self.driver)


class UserPost(Component):
	POST_CONTROLS_LIST_WRAPPER = '//div[@class="feed_f"]'
	POST_CONTROLS_LIST = '//li[@class="widget-list_i"]'
	POST_CONTROL_ADD_COMMENT = '//a[@class="h-mod widget_cnt"]'
	POST_CONTROL_REPOST = '//div[@class="widget_cnt"]'
	POST_CONTROL_CLASS = '//div[@class="widget_cnt"]'

	POST = '//a[@href="/profile/570965755234/statuses/67241421616482"]'

	def get_post(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_elements_by_xpath(self.POST_IMG)
		)

	def get_post_controls(self):
		post = self.get_post()[1]
		post_controls_wrapper = post.find_element_by_xpath(self.POST_CONTROLS_LIST_WRAPPER)

		return post_controls_wrapper.find_elements_by_xpath(self.POST_CONTROLS_LIST)

	def get_post_control_add_comments(self):
		controls = self.get_post_controls()[0]

		return controls.find_element_by_xpath(self.POST_CONTROL_ADD_COMMENT).find_element_by_class_name('widget_ico')
