from components.contacts.confirm_phone_popup_component import ConfirmPhonePopup
from components.contacts.delete_email_popup_component import ContactsDeleteEmailPopup
from components.contacts.delete_phone_popup_component import ContactsDeletePhonePopup
from components.contacts.email_popup_component import ContactsEmailPopup
from components.contacts.main_block_component import ContactsMainBlock
from components.contacts.phone_popup_component import ContactsPhonePopup
from pages.base_page import Page


class ContactsPage(Page):
    PATH = 'contacts/'

    @property
    def main_page(self):
        return ContactsMainBlock(self)

    @property
    def pop_up_phone(self):
        return ContactsPhonePopup(self)

    @property
    def pop_up_delete_phone(self):
        return ContactsDeletePhonePopup(self)

    @property
    def pop_up_delete_email(self):
        return ContactsDeleteEmailPopup(self)

    @property
    def pop_up_email(self):
        return ContactsEmailPopup(self)

    @property
    def pop_up_confirm_phone(self):
        return ConfirmPhonePopup(self)
