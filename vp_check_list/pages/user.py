# -*- coding: utf-8 -*-

import os

from vp_check_list.elements.avatar import UserAvatar
from vp_check_list.elements.user import UserHeader, AuthForm
from vp_check_list.pages.base import Page


class AuthPage(Page):
	PATH = ''

	@property
	def form(self):
		return AuthForm(self.driver)

	def login(self):
		user_login = 'technopark34'
		password = os.environ['OK_PASSWORD']

		auth_form = self.form
		auth_form.set_login(user_login)
		auth_form.set_password(password)
		auth_form.submit()


class UserPage(Page):
	PATH = ''

	def login(self):
		auth_page = AuthPage(self.driver)

		auth_page.open()
		auth_page.login()

		return self.user_header.get_username()

	@property
	def avatar(self):
		return UserAvatar(self.driver)

	@property
	def user_header(self):
		return UserHeader(self.driver)
