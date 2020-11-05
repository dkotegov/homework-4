# coding=utf-8
import time

from selenium.webdriver.support.wait import WebDriverWait

from components.contacts_form import ContactsForm
from .base import Page


class ContactAddingPage(Page):
    """
    Страница добавления контакта
    """

    def __init__(self, driver):
        super(ContactAddingPage, self).__init__(driver)

        self.contact_form = ContactsForm(self.driver)

    def create_contact(self, **kwargs):
        self.contact_form.click_create_contact()

        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()

    def try_to_create_empty_contact(self):
        self.contact_form.click_create_contact()
        self.contact_form.fill_form()
        self.contact_form.click_save()

    def has_error(self):
        return self.contact_form.check_edit_error()

    def has_validation_errors(self):
        return self.contact_form.check_validation_error()

    def has_any_error(self):
        return self.has_error() or self.contact_form.check_validation_error()

    def contacts_exist(self, emails):
        return self.contact_form.contacts_exists(emails)

    def contact_exists(self, email):
        return self.contact_form.contacts_exists([email])

    def delete_all_contacts(self):
        return self.contact_form.delete_contacts_if_needed()

    def return_back(self):
        return self.contact_form.click_return_if_exists()

    def wait_for_return_back(self):
        return self.contact_form.click_return()