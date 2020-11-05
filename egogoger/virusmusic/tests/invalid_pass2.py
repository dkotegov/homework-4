from egogoger.virusmusic.pages.main_page import MainPage
from egogoger.base_test import Test
from .open_reg_form import open_reg_form
from egogoger.utils import set_input


class InvalidPassword2Test(Test):
	# Correct messages
	PASSWORD_ERROR = 'Passwords must match'

	CORRECT_PASS = 'kek'
	INCORRECT_PASS = 'l'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		set_input(self.driver, form.PASSWORD, self.CORRECT_PASS)
		set_input(self.driver, form.PASSWORD2, self.INCORRECT_PASS)
		form.submit()
		form.check_error_msg_for(form.PASSWORD_ERROR, self, self.PASSWORD_ERROR)
