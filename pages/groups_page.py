from .base import Page
from components.groups_form import GroupsForm
from components.contacts_form import ContactsForm


class GroupsPage(Page):

    def __init__(self, driver):
        super(GroupsPage, self).__init__(driver)

        self.groups = GroupsForm(self.driver)
        self.contacts = ContactsForm(self.driver)

    def create_group(self, name):
        self.groups.click_dropdown()
        self.groups.click_create_group()
        self.groups.input_group_name(name)
        self.groups.click_save()

    def create_group_from_contact_page(self, email, name):
        self.groups.click_group_block('allContacts')
        self.contacts.click_contact_block(email)
        self.contacts.click_to_group()
        self.groups.click_create_group_from_contact_page()
        self.groups.input_group_name(name)
        self.groups.click_save()

    def open_create_popup(self):
        self.groups.click_dropdown()
        self.groups.click_create_group()

    def create_group_popup_exists(self):
        return self.groups.group_popup_exists()

    def cancel_group_editing(self):
        self.groups.click_cancel()

    def change_group_name(self, id, name):
        self.groups.click_settings(id)
        if name != '':
            self.groups.input_group_name(name)
        else:
            self.groups.clear_group_name()
        self.groups.click_save()

    def open_change_popup(self, id):
        self.groups.click_settings(id)

    def delete_group(self, id):
        if not self.groups.click_settings(id):
            self.groups.click_settings(id)
        self.groups.delete_group()

    def delete_all_groups(self):
        ids = self.groups.get_group_ids()
        for id in ids:
            self.delete_group(id)

    def group_exists(self, id):
        return self.groups.group_exists(id)

    def group_name_exists(self, id, name):
        return self.groups.group_name_exists(id, name)

    def error_exists(self):
        return self.groups.error_exists()

    def create_contact(self, email):
        self.groups.click_group_block('allContacts')
        self.contacts.click_create_contact()
        self.contacts.input_email(email)
        self.contacts.click_save()
        self.contacts.click_return_if_exists()
        self.groups.click_group_block('allContacts')

    def create_contact_without_email(self, firstname):
        self.groups.click_group_block('allContacts')
        self.contacts.click_create_contact()
        self.contacts.input_firstname(firstname)
        self.contacts.click_save()
        self.contacts.click_return_if_exists()
        self.groups.click_group_block('allContacts')

    def delete_all_contacts(self):
        if self.contacts.click_select_all():
            self.contacts.delete_contacts()

    def contacts_exists(self, emails, id):
        self.groups.click_group_block(id)
        if self.contacts.contacts_exists(emails):
            return True
        self.driver.refresh()
        self.groups.click_group_block(id)
        return self.contacts.contacts_exists(emails)

    def add_contact_to_groups(self, email, ids):
        self.groups.click_group_block('allContacts')
        self.contacts.click_contact_block(email)
        self.contacts.click_to_group()
        self.contacts.select_groups(ids)
        self.contacts.click_apply()
        self.contacts.click_return_if_exists()

    def add_all_contacts_to_groups(self, ids):
        self.groups.click_group_block('allContacts')
        self.contacts.click_select_all()
        self.contacts.click_to_group()
        self.contacts.select_groups(ids)
        self.contacts.click_apply()

    def add_selected_contacts_to_group(self, emails, ids):
        self.groups.click_group_block('allContacts')
        self.contacts.select_contacts(emails)
        self.contacts.click_to_group()
        self.contacts.select_groups(ids)
        self.contacts.click_apply()
