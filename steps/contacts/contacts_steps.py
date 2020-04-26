import os

from steps.base_steps import BaseSteps
from pages.contacts.contacts_page import ContactsPage


class ContactsSteps(BaseSteps):

    def __init__(self, driver, page=None):
        super().__init__(driver, ContactsPage)

    # 1.func_phone

    def func_add_number(self, phone):
        self.open()
        main_page = self.page.main_page
        main_page.add_phone(phone)

    def func_delete_number(self):
        self.open()
        main_page = self.page.main_page
        main_page.delete_phone()

    def func_delete_reserved_number(self):
        self.open()
        main_page = self.page.main_page
        main_page.delete_phone_reserved()

    # 2.func_email

    def func_add_email(self, email):
        self.open()
        main_page = self.page.main_page
        main_page.add_email_check(email)

    def func_delete_email(self):
        self.open()
        main_page = self.page.main_page
        main_page.delete_email()

    # 3.add_phone_popup

    def add_phone_popup_valid_number(self, phone):
        self.open()
        main_page = self.page.main_page
        main_page.add_valid_phone(phone)

    def add_phone_popup_invalid_number(self, phone):
        self.open()
        main_page = self.page.main_page
        main_page.add_invalid_phone(phone)

    def add_phone_popup_change_country(self):
        self.open()
        main_page = self.page.main_page
        main_page.open_popup_phone()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.change_country()

    def add_phone_popup_cancel(self):
        self.open()
        main_page = self.page.main_page
        main_page.open_popup_phone()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.cancel()

    def add_phone_popup_close(self):
        self.open()
        main_page = self.page.main_page
        main_page.open_popup_phone()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.close()

    # 4.confirm_phone_popup

    def confirm_phone_popup_invalid_code(self, phone, code):
        self.add_phone_popup_valid_number(phone)
        pop_up_confirm_phone = self.page.pop_up_confirm_phone
        pop_up_confirm_phone.check_code_invalid(code)

    def confirm_phone_popup_empty_code(self, phone):
        self.add_phone_popup_valid_number(phone)
        pop_up_confirm_phone = self.page.pop_up_confirm_phone
        pop_up_confirm_phone.check_code_empty()

    def confirm_phone_popup_close(self, phone):
        self.add_phone_popup_valid_number(phone)
        pop_up_confirm_phone = self.page.pop_up_confirm_phone
        pop_up_confirm_phone.close()

    def confirm_phone_popup_change_number(self, phone):
        self.add_phone_popup_valid_number(phone)
        pop_up_confirm_phone = self.page.pop_up_confirm_phone
        pop_up_confirm_phone.change_number()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.wait_for_container()

    # 5.add_email_popup

    def add_email_popup_invalid_email(self, email):
        self.open()
        main_page = self.page.main_page
        main_page.add_invalid_email(email)

    def add_email_popup_valid_email(self, email):
        self.open()
        main_page = self.page.main_page
        main_page.add_valid_email(email)

    def add_email_popup_cancel(self):
        self.open()
        main_page = self.page.main_page
        main_page.open_popup_email()
        open_popup_email = self.page.pop_up_email
        open_popup_email.cancel()

    def add_email_popup_close(self):
        self.open()
        main_page = self.page.main_page
        main_page.open_popup_email()
        open_popup_email = self.page.pop_up_email
        open_popup_email.close()

    # 6.data_saving
    def refresh_page_add_email(self, email):
        self.func_add_email(email)
        self.open()
        main_page = self.page.main_page
        main_page.check_email(email)




