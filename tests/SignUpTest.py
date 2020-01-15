# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.SignUpPage import SignUpPage
from pages.MainPage import MainPage

import datetime


class SignUpTest(BasicTest):
	error_firstname = 'Enter your first name'
	error_lastname = 'Enter your last name'
	error_birthdate = 'Enter your birth date'
	error_sex = 'Enter your gender'
	error_email = u'Укажите желаемое имя аккаунта'
	error_password_empty = 'Enter your password'
	error_short_password = 'Use at least 8 characters'
	error_future_date = 'Marty, the time machine hasn\'t been invented yet. Select a different date.'
	error_various_passwords = 'The passwords don\'t match'

	def setUp(self):
		super(SignUpTest, self).setUp()
		self.signup_page = SignUpPage(self.driver)
		self.signup_page.open()

	def test_correct_registration(self):
		email = self.signup_page.generate_fake_email()
		password = self.signup_page.generate_fake_password()

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": 4,
			"month": "April",
			"year": 2000,
			"sex": "male",
			"email": email,
			"domain": "mail",
			"password": password,
			"password_retry": password
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		self.signup_page.wait_redirect(self.SIGNUP_VERIFY_URL)

	def test_empty_data(self):
		data = {}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		elem_err_firstname = self.signup_page.wait_render(self.signup_page.error_message(self.error_firstname))
		self.assertEqual(self.error_firstname, elem_err_firstname.text)

		elem_err_lastname = self.signup_page.wait_render(self.signup_page.error_message(self.error_lastname))
		self.assertEqual(self.error_lastname, elem_err_lastname.text)

		elem_err_birthdate = self.signup_page.wait_render(self.signup_page.error_message(self.error_birthdate))
		self.assertEqual(self.error_birthdate, elem_err_birthdate.text)

		elem_err_sex = self.signup_page.wait_render(self.signup_page.error_message(self.error_sex))
		self.assertEqual(self.error_sex, elem_err_sex.text)

		elem_err_email = self.signup_page.wait_render(self.signup_page.error_message(self.error_email))
		self.assertEqual(self.error_email, elem_err_email.text)

		elem_err_password_empty = self.signup_page.wait_render(self.signup_page.error_message(self.error_password_empty))
		self.assertEqual(self.error_password_empty, elem_err_password_empty.text)

	def test_future_date(self):
		email = self.signup_page.generate_fake_email()
		password = self.signup_page.generate_fake_password()
		tomorrow = datetime.date.today() + datetime.timedelta(days=1)
		year = int(tomorrow.strftime('%Y'))
		month = tomorrow.strftime('%B')
		day = int(tomorrow.strftime('%d'))

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": day,
			"month": month,
			"year": year,
			"sex": "male",
			"email": email,
			"domain": "bk",
			"password": password,
			"password_retry": password
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		elem_err = self.signup_page.wait_render(self.signup_page.error_message(self.error_future_date))
		self.assertEqual(self.error_future_date, elem_err.text)

	def test_short_password(self):
		email = self.signup_page.generate_fake_email()

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": 4,
			"month": "April",
			"year": 2000,
			"sex": "male",
			"email": email,
			"domain": "mail",
			"password": '1',
			"password_retry": '1'
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		elem_err = self.signup_page.wait_render(self.signup_page.error_message(self.error_short_password))
		self.assertEqual(self.error_short_password, elem_err.text)

	def test_user_exists(self):
		existing_login = 'TPWAO'
		password = self.signup_page.generate_fake_password()

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": 4,
			"month": "April",
			"year": 2000,
			"sex": "male",
			"email": existing_login,
			"domain": "mail",
			"password": password,
			"password_retry": password
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		email_err_popup = self.signup_page.wait_render(self.signup_page.email_popup_message)

		expected_message = u'Аккаунт с таким именем уже существует.\nYou might like these email addresses:'

		self.assertEqual(expected_message, email_err_popup.text)

	def test_incorrect_login(self):
		incorrect_login = 'TPWAO@'
		password = self.signup_page.generate_fake_password()

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": 4,
			"month": "April",
			"year": 2000,
			"sex": "male",
			"email": incorrect_login,
			"domain": "mail",
			"password": password,
			"password_retry": password
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		email_err_popup = self.signup_page.wait_render(self.signup_page.email_popup_message)

		expected_message = u'Некорректное имя аккаунта. Допустимо использовать только латинские буквы, цифры,\nзнак подчеркивания («_»), точку («.»), минус («-»)'

		self.assertEqual(expected_message, email_err_popup.text)

	def test_various_passwords(self):
		email = self.signup_page.generate_fake_email()
		password1 = self.signup_page.generate_fake_password()
		password2 = password1 + '1'

		data = {
			"firstname": '1',
			"lastname": '2',
			"day": 4,
			"month": "April",
			"year": 2000,
			"sex": "male",
			"email": email,
			"domain": "mail",
			"password": password1,
			"password_retry": password2
		}

		self.signup_page.enter_signup_data(data)
		self.signup_page.click_signup()

		elem_err = self.signup_page.wait_render(self.signup_page.error_message(self.error_various_passwords))
		self.assertEqual(self.error_various_passwords, elem_err.text)
