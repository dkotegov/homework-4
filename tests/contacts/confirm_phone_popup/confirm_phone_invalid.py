from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class ConfirmPopupPhoneInvalidTest(BaseTest):
    CODE = '9999999999999999'
    PHONE = '+79191118356'

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).confirm_phone_popup_invalid_code(self.PHONE, self.CODE)
