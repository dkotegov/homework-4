import unittest

from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class FuncAddEmailSecondTest(BaseTest):
    EMAIL = 'spiridonova.alex@yandex.ru'

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).func_add_email(self.EMAIL)
