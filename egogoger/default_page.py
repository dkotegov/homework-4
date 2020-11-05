class DefaultPage:
	PATH = ''

	def __init__(self, driver, path):
		self.driver = driver
		self.PATH = path

	def open(self):
		self.driver.get(self.PATH)
		self.driver.maximize_window()


class Component:
	def __init__(self, driver):
		self.driver = driver
