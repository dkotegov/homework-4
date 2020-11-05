# coding=utf-8
import time

from components.contacts_form import ContactsForm
from pages.base import Page


class ContactEditPage(Page):
    """
    Страница изменения контакта
    """

    def __init__(self, driver):
        super(ContactEditPage, self).__init__(driver)

        self.contact_form = ContactsForm(self.driver)

    def create_contact(self, **kwargs):
        self.contact_form.click_create_contact()

        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()

    def edit_contact(self, **kwargs):
        self.contact_form.click_edit_contact()

        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()

    def has_error(self):
        return self.contact_form.check_edit_error()
