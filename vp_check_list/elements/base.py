# -*- coding: utf-8 -*-


class Component(object):
	def __init__(self, driver):
		self.driver = driver

	def execute(self, component):
		self.driver.execute_script('arguments[0].click();', component)

	def get_text(self, component):
		return component.get_attribute("textContent")

	def set_text_content(self, component, message):
		self.driver.execute_script("arguments[0].textContent = '{}';".format(message), component)
