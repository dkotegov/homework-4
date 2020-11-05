from .base import Page
from components.groups_form import GroupsForm
from components.contacts_form import ContactsForm


class FavoritesPage(Page):

    def __init__(self, driver):
        super(FavoritesPage, self).__init__(driver)

        self.groups = GroupsForm(self.driver)
        self.contacts = ContactsForm(self.driver)

    def add_to_favorites_from_contact_page(self, email):
        self.groups.click_group_block('allContacts')
        self.contacts.click_contact_block(email)
        self.contacts.click_favorites()

    def add_to_favorites_from_star_in_contact_list(self, email):
        self.contacts.click_star_on_contact_list(email)
