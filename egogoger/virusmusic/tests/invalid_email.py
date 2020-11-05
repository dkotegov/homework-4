from egogoger.virusmusic.pages.main_page import MainPage
from egogoger.base_test import Test
from .open_reg_form import open_reg_form
from egogoger.utils import set_input


class InvalidEmailTest(Test):
	# Correct messages
	EMAIL_ERROR = 'Incorrect email syntax'

	# Incorrect cases
	SHORT_NAME = 'kek'
	DOMAIN_ONLY = '@mail.ru'

	# Correct cases
	CYRILLIC_NAME = 'кек@мэйл.ру'
	LONG_NAME = 'a' * 257 + '@mail.ru'
	NUMERIC_NAME = '123' + '@mail.ru'
	BAD_DOMAIN1 = 'kek@mail'
	BAD_DOMAIN2 = 'kek@mail.'
	BAD_NAME1 = '.' + '@mail.ru'
	BAD_NAME2 = '.@m.u'


	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		bad_cases = [self.SHORT_NAME, self.DOMAIN_ONLY]
		good_cases = [self.CYRILLIC_NAME, self.LONG_NAME, self.NUMERIC_NAME, self.BAD_DOMAIN1, self.BAD_DOMAIN2, self.BAD_NAME1, self.BAD_NAME2]

		for case in bad_cases:
			set_input(self.driver, form.EMAIL, case)
			form.submit()
			form.check_error_msg_for(form.EMAIL_ERROR, self, self.EMAIL_ERROR)

		for case in good_cases:
			set_input(self.driver, form.EMAIL, case)
			form.submit()
			form.check_error_msg_for(form.EMAIL_ERROR, self, None)
