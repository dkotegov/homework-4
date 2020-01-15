# -*- coding: utf-8 -*-
import random

from BasicPage import BasicPage


class SignUpPage(BasicPage):
	firstname_field = 'input[name="firstname"]'
	lastname_field = 'input[name="lastname"]'
	day_block = '.b-date__day'
	month_block = '.b-date__month'
	year_block = '.b-date__year'
	sex_male_input = 'label[data-mnemo="sex-male"]'
	sex_female_input = 'label[data-mnemo="sex-female"]'
	email_field = 'input[data-blockid="email_name"]'
	email_block = 'div[type="email"] .b-email__domain'
	email_input_mail = 'a[data-text="@mail.ru"]'
	email_input_inbox = 'a[data-text="@inbox.ru"]'
	email_input_list = 'a[data-text="@list.ru"]'
	email_input_bk = 'a[data-text="@bk.ru"]'
	password_field = 'input[name="password"]'
	password_retry_field = 'input[name="password_retry"]'
	password_show_block = '.b-password__eye'
	password_hide_block = '.b-password__eye.b-password__eye_active'
	button_signup = 'button[data-bem="btn"]'
	additional_email_block = 'a.js-signup-simple-link'
	additional_email_field = 'input[name="additional_email"][tabindex="9"]'
	additional_phone_block = 'a.js-signup-link'
	email_popup_message = '.b-vacant-email__message'
	password_popup_message = '.b-password__status-text b-password__status-text_'
	error_blocks = '.b-form-field__errors__error.js-required.b-form-field__errors__error_visible'

	unit_to_multiplier = {
		"mail": email_input_mail,
		"inbox": email_input_inbox,
		"list": email_input_list,
		"bk": email_input_bk
	}

	def day_input(self, day):
		return ('a[data-text="' + str(day) + '"]')

	def month_input(self, month):
		return ('a[data-text="' + month + '"]')

	def year_input(self, year):
		return ('a[data-text="' + str(year) + '"]')

	def error_message(self, text):
		return ('div[data-text="' + text + '"]')

	def open(self):
		self.driver.get(self.SIGNUP_URL)

	def enter_firstname(self, firstname):
		elem = self.wait_render(self.firstname_field)
		elem.send_keys(firstname)

	def enter_lastname(self, lastname):
		elem = self.wait_render(self.lastname_field)
		elem.send_keys(lastname)

	def enter_day(self, day):
		elem = self.wait_render(self.day_block)
		elem.click()
		elem = self.wait_render(self.day_input(day))
		elem.click()

	def enter_month(self, month):
		elem = self.wait_render(self.month_block)
		elem.click()
		elem = self.wait_render(self.month_input(month))
		elem.click()

	def enter_year(self, year):
		elem = self.wait_render(self.year_block)
		elem.click()
		elem = self.wait_render(self.year_input(year))
		elem.click()

	def click_sex_male(self):
		elem = self.wait_render(self.sex_male_input)
		elem.click()

	def click_sex_female(self):
		elem = self.wait_render(self.sex_female_input)
		elem.click()

	def enter_email(self, email):
		elem = self.wait_render(self.email_field)
		elem.send_keys(email)

	def enter_emaildomain(self, emaildomain):
		elem = self.wait_render(self.email_block)
		elem.click()
		elem = self.wait_render(self.unit_to_multiplier[emaildomain])
		elem.click()

	def enter_password(self, password):
		elem = self.wait_render(self.password_field)
		elem.send_keys(password)

	def enter_password_retry(self, password):
		elem = self.wait_render(self.password_retry_field)
		elem.send_keys(password)

	def show_password(self):
		elem = self.wait_render(self.password_show_block)
		elem.click()

	def hide_password(self):
		elem = self.wait_render(self.password_hide_block)
		elem.click()

	def click_additionalemail(self):
		elem = self.wait_render(self.additional_email_block)
		elem.click()

	def click_additionalphone(self):
		elem = self.wait_render(self.additional_phone_block)
		elem.click()

	def enter_additionalemail(self, email):
		elem = self.wait_render(self.additional_email_field)
		elem.send_keys(email)

	def click_signup(self):
		elem = self.wait_render(self.button_signup)
		elem.click()

	def enter_signup_data(self, data):
		if 'firstname' in data:
			self.enter_firstname(data['firstname'])

		if 'lastname' in data:
			self.enter_lastname(data['lastname'])

		if 'day' in data:
			self.enter_day(data['day'])

		if 'month' in data:
			self.enter_month(data['month'])

		if 'year' in data:
			self.enter_year(data['year'])

		if ('sex' in data):
			if (data['sex'] == 'male'):
				self.click_sex_male()
			elif (data['sex'] == 'female'):
				self.click_sex_female()

		if 'email' in data:
			self.enter_email(data['email'])

		if 'domain' in data:
			self.enter_emaildomain(data['domain'])

		if 'password' in data:
			self.enter_password(data['password'])

		if 'password_retry' in data:
			self.enter_password_retry(data['password_retry'])

		self.click_additionalemail()
		if 'addition_email' in data:
			self.enter_additionalemail(data['addition_email'])

	def generate_fake_email(self):
		return ('waocustom_email' + str(random.randrange(1, 10000000)))

	def generate_fake_password(self):
		return ('CooL!WaOPaSs' + str(random.randrange(1, 10000000)) + '!_1A')
