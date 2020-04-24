from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class FuncDeletePhoneReservedTest(BaseTest):

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).func_delete_reserved_number()
