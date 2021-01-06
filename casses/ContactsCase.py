import unittest

from casses.base.BaseTest import BaseTest
from pages.ContactsPage import ContactsPage


class ContactsTest(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        super(ContactsTest, self).setUp()
        contacts_page = ContactsPage(self.driver)
        contacts_page.open()
        self.page = ContactsPage(self.driver)

    def tearDown(self) -> None:
        super(ContactsTest, self).tearDown()

    def test_add_email_button(self) -> None:
        self.page.open_add_email_popup()
        self.assertTrue(self.page.is_add_email_popup_open())

    def test_add_phone_button(self) -> None:
        self.page.open_add_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_open())

    def test_delete_email(self) -> None:
        self.page.open_add_email_popup()
        self.page.add_backup_email("test_login_a.elagin1@mail.ru")
        self.page.open()
        self.page.delete_email()
        self.assertTrue(self.page.has_not_backup_email())

    def test_invalid_phone(self) -> None:
        self.page.open_add_phone_popup()
        self.page.send_phone('1231')
        self.assertTrue(self.page.is_phone_error())

    def test_close_phone_popup(self) -> None:
        self.page.open_add_phone_popup()
        self.page.close_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_close())

    def test_cancel_phone_popup(self) -> None:
        self.page.open_add_phone_popup()
        self.page.cancel_phone_popup()
        self.assertTrue(self.page.is_add_phone_popup_close())
