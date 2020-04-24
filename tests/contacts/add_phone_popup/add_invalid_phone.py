from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class AddPopupPhoneInvalidTest(BaseTest):
    PHONE = '+79999999999999999'

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).add_phone_popup_invalid_number(self.PHONE)
