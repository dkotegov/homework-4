# -*- coding: utf-8 -*-

import urlparse


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

	def get_text(self, component):
		return component.get_attribute("textContent")

	def set_text_content(self, component, message):
		self.driver.execute_script("arguments[0].textContent = '{}';".format(message), component)
