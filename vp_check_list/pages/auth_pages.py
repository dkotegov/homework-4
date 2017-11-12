# -*- coding: utf-8 -*-
import os

from selenium.webdriver.support.ui import WebDriverWait

from vp_check_list.pages.pages import Page, Component


class AuthPage(Page):
	PATH = ''

	@property
	def form(self):
		return AuthForm(self.driver)

	@property
	def top_menu(self):
		return UserHeader(self.driver)


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

	def login(self):
		user_login = 'technopark34'
		password = os.environ['OK_PASSWORD']

		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(user_login)
		auth_form.set_password(password)
		auth_form.submit()

		return auth_page.top_menu.get_username()


class UserHeader(Component):
	USERNAME = '//h1[@class="mctc_name_tx bl"]'

	def get_username(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.USERNAME).text
		)
