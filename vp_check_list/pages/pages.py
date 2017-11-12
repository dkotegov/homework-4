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

	def execute(self, component):
		self.driver.execute_script('arguments[0].click();', component)


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
	POST = '//a[@href="/profile/570965755234/statuses/67241421616482"]'
	POST_COMMENT_INPUT = '//div[@class="itx js-comments_add js-ok-e comments_add-ceditable "]'
	POST_COMMENT_BUTTON = '//button[@class="button-pro form-actions_yes"]'
	POST_COMMENT_LAST = '//div[@class=" last-comment"]'
	POST_COMMENT_TEXT = '//div[@class="comments_text textWrap"]'
	POST_COMMENT_CONTROL = '//div[@class="comments_controls-t"]'
	POST_COMMENT_CONTROL_DELETE = '//a[@title="Удалить"]'

	def set_text_content(self, component, message):
		self.driver.execute_script("arguments[0].textContent = '{}';".format(message), component)

	def get_post(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_elements_by_xpath(self.POST)
		)

	def get_comment_input(self, post):
		return WebDriverWait(post, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.POST_COMMENT_INPUT)
		)

	def open_post(self):
		user_post = self.get_post()[0]
		self.execute(user_post)

		return user_post

	def add_comment(self, message):
		user_post = self.open_post()
		comment_input = self.get_comment_input(user_post)

		self.execute(comment_input)
		self.set_text_content(comment_input, message)

		button = self.driver.find_element_by_xpath(self.POST_COMMENT_BUTTON)
		self.execute(button)

	def get_comment_component(self):
		user_post = self.open_post()

		return user_post.find_element_by_xpath(self.POST_COMMENT_LAST)

	def get_comment_text(self):
		last_comment_wrapper = self.get_comment_component()

		# .text not work
		comment = last_comment_wrapper.find_element_by_xpath(self.POST_COMMENT_TEXT)\
			.find_element_by_tag_name('div').get_attribute("textContent")

		return comment

	def del_comment(self):
		last_comment_wrapper = self.get_comment_component()
		controls_wrapper = last_comment_wrapper.find_element_by_xpath(self.POST_COMMENT_CONTROL)

		print controls_wrapper


