from egogoger.virusmusic.pages.main_page import MainPage
from egogoger.base_test import Test
from .open_reg_form import open_reg_form
from egogoger.utils import set_input


class EmptyFieldsTest(Test):
	# Correct messages
	EMPTY_NAME_ERROR = 'Enter your name'
	EMPTY_LOGIN_ERROR = 'Enter login'
	EMPTY_EMAIL_ERROR = 'Enter email'
	EMPTY_PASSWORD_ERROR = 'Enter password'
	EMPTY_PASSWORD2_ERROR = 'Repeat the password'

	# tmp messages
	TMP_PASSWORD = 'kek8971364'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

        # All fields empty
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, self.EMPTY_NAME_ERROR)
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.EMPTY_LOGIN_ERROR)
		form.check_error_msg_for(form.EMAIL_ERROR, self, self.EMPTY_EMAIL_ERROR)
		form.check_error_msg_for(form.PASSWORD_ERROR, self, self.EMPTY_PASSWORD_ERROR)

		# Second password empty
		set_input(self.driver, form.PASSWORD, self.TMP_PASSWORD)
		form.submit()
		form.check_error_msg_for(form.PASSWORD_ERROR, self, self.EMPTY_PASSWORD2_ERROR)
