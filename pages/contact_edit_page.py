# coding=utf-8
import time

from components.contacts_form import ContactsForm
from components.remove_contact_form import RemoveContactForm
from pages.base import Page


class ContactEditPage(Page):
    """
    Страница изменения контакта
    """

    def __init__(self, driver):
        super(ContactEditPage, self).__init__(driver)

        self.contact_form = ContactsForm(self.driver)
        self.removal_form = RemoveContactForm(self.driver)

    def create_contact(self, **kwargs):
        self.contact_form.click_create_contact()

        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()

    def edit_contact(self, **kwargs):
        self.contact_form.click_edit_contact()

        self.contact_form.fill_form(**kwargs)

        self.contact_form.click_save()

    def fill_form_and_save(self, **kwargs):
        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()

    def delete_all_contacts(self):
        return self.contact_form.delete_contacts_if_needed()

    def has_error(self):
        return self.contact_form.check_edit_error()

    def delete_contact(self):
        self.contact_form.click_remove_contact()
        self.removal_form.confirm_removal()

    def has_validation_errors(self):
        return self.contact_form.check_validation_error()

    def return_back(self):
        return self.contact_form.click_return_if_exists()

    def contact_exists(self, email):
        return self.contact_form.contacts_exists([email])

    def has_any_error(self):
        return self.has_error() or self.contact_form.check_validation_error()

