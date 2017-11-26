# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from vp_check_list.elements.base import Component


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
