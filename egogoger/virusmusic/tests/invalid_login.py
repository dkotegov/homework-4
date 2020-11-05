from egogoger.virusmusic.pages.main_page import MainPage
from egogoger.virusmusic.utils import get_datetime
from egogoger.virusmusic.constants import BACKEND_ERROR
from egogoger.base_test import Test
from .open_reg_form import open_reg_form
from egogoger.utils import set_input


class InvalidLoginTest(Test):
	# Correct messages
	LOGIN_ERROR = 'Login must contain at least 3 letters or numbers'

	CYRILLIC_NAME = 'Вася'
	CYRILLIC_WITH_NUMBERS_NAME = CYRILLIC_NAME+'1'
	SHORT_NAME = 'ke'
	LONG_NAME = 'a' * 257
	NUMERIC_NAME = '123'


	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)
		form.clear_inputs()

		# Cyrillic name
		set_input(self.driver, form.LOGIN, self.CYRILLIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Cyrillic with numbers name
		set_input(self.driver, form.LOGIN, self.CYRILLIC_WITH_NUMBERS_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Short name
		set_input(self.driver, form.LOGIN, self.SHORT_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Numeric name
		set_input(self.driver, form.LOGIN, self.NUMERIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, None)
		form.clear_inputs()

		# Long name (BACKEND check)
		form.set_correct_values()
		set_input(self.driver, form.LOGIN, self.LONG_NAME)
		form.submit()
		form.check_error_msg_for(form.BACKEND_ERROR, self, BACKEND_ERROR)
		form.clear_inputs()
