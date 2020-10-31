from .base import Page
from components.contacts_form import ContactsForm


class ContactsPage(Page):

    def __init__(self, driver):
        super(ContactsPage, self).__init__(driver)

        self.form = ContactsForm(self.driver)

    def create_group(self, name):
        self.form.click_dropdown()
        self.form.create_group()
        self.form.input_group_name(name)
        self.form.click_save()

    def delete_group(self, id):
        self.form.click_settings(id)
        self.form.delete()

    def delete_all_groups(self):
        ids = self.form.get_group_ids()
        for id in ids:
            self.delete_group(id)

    def change_group_name(self, id, name):
        self.form.click_settings(id)
        if name != '':
            self.form.input_group_name(name)
        else:
            self.form.clear_group_name_input()
        self.form.click_save()

    def check_group(self, id):
        self.form.check_group(id)

    def check_group_name(self, id, name):
        return self.form.check_group_name(id, name)

    def error_exists(self):
        return self.form.error_exists()

    def cancel_create(self):
        self.form.click_cancel()
