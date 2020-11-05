from egogoger.virusmusic.pages.main_page import MainPage
from egogoger.virusmusic.constants import BACKEND_ERROR
from egogoger.base_test import Test
from .open_reg_form import open_reg_form
from egogoger.utils import set_input


class InvalidNameTest(Test):
	CYRILLIC_NAME = 'Вася'
	SHORT_NAME = '1'
	LONG_NAME = 'a' * 257

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)
		form.clear_inputs()

		# Cyrillic name
		set_input(self.driver, form.NAME, self.CYRILLIC_NAME)
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, None)
		form.clear_inputs()

		# Short name
		set_input(self.driver, form.NAME, self.SHORT_NAME)
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, None)
		form.clear_inputs()

		# BACKEND checks
		## Long name
		form.set_correct_values()
		set_input(self.driver, form.NAME, self.LONG_NAME)
		form.submit()
		form.check_error_msg_for(form.BACKEND_ERROR, self, BACKEND_ERROR)
		form.clear_inputs()
