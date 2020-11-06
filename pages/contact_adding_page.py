# coding=utf-8
import time

from selenium.webdriver.support.wait import WebDriverWait

from components.contacts_form import ContactsForm
from components.groups_form import GroupsForm
from .base import Page


class ContactAddingPage(Page):
    """
    Страница добавления контакта
    """

    def __init__(self, driver):
        super(ContactAddingPage, self).__init__(driver)

        self.contact_form = ContactsForm(self.driver)
        self.group_form = GroupsForm(self.driver)

    def create_contact(self, close=True, **kwargs):
        self.group_form.click_group_block('allContacts')
        self.contact_form.click_create_contact()
        self.contact_form.fill_form(**kwargs)
        self.contact_form.click_save()
        if close:
            self.contact_form.click_return_if_exists()
            self.group_form.click_group_block('allContacts')

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
        if self.contact_form.click_select_all():
            self.contact_form.delete_contacts()

    def return_back(self):
        return self.contact_form.click_return_if_exists()

    def wait_for_return_back(self):
        return self.contact_form.click_return_if_exists()

    def open_contact_page(self, email):
        self.contact_form.click_contact_block(email)
