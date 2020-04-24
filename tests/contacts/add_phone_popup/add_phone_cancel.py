from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class AddPopupPhoneCancelTest(BaseTest):

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).add_phone_popup_cancel()
