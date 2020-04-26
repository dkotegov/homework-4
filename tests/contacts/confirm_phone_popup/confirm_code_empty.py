from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class ConfirmPopupPhoneEmptyTest(BaseTest):
    PHONE = '+79191118356'

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).confirm_phone_popup_empty_code(self.PHONE)
