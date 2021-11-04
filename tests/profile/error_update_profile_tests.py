import os

import constants
from pages.profile import ProfilePage
from components.profile_form import ProfileForm
from tests.default_authorized import TestAuthorized


class ChangeToInvalidLoginTest(TestAuthorized):
    INVALID_LOGIN = 'testqa@'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )


class ChangeToEmptyLoginTest(TestAuthorized):
    EMPTY_LOGIN = ''

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.EMPTY_LOGIN)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_EMPTY_UPD_LOGIN
        )


class ChangeToInvalidEmailTest(TestAuthorized):
    INVALID_EMAIL = 'testqa$$@mail.ru'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_email(self.INVALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_email_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_EMAIL
        )


class ChangeToEmptyEmailTest(TestAuthorized):
    EMPTY_EMAIL = ''

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_email(self.EMPTY_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_email_error(),
            constants.ERROR_MSG_OF_EMPTY_UPD_EMAIL
        )


class ChangeToInvalidEmailAndLoginTest(TestAuthorized):
    INVALID_LOGIN = 'testqa@'
    INVALID_EMAIL = 'testqa$$@mail.ru'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.set_email(self.INVALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )


class ChangeToInvalidLoginAndValidEmailTest(TestAuthorized):
    INVALID_LOGIN = 'testqa@'
    NEW_VALID_EMAIL = 'newvalidemail@mail.ru'

    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_form = ProfileForm(self.driver)
        profile_form.set_login(self.INVALID_LOGIN)
        profile_form.set_email(self.NEW_VALID_EMAIL)
        profile_form.submit()

        self.assertEqual(
            profile_form.get_login_error(),
            constants.ERROR_MSG_OF_INVALID_UPD_LOGIN
        )