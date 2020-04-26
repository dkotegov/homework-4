from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class ChangeDataRefreshTest(BaseTest):
    EMAIL = 'abcd@gmail.com'

    def test(self):
        AuthSteps(self.driver).auth()

        ContactsSteps(self.driver).refresh_page_add_email(self.EMAIL)


