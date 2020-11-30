from pages.BasePage import Page
from steps.ContactsSteps import ContactsSteps


class ContactsPage(Page):
    PATH = "contacts"

    def open_add_phone_popup(self) -> None:
        contacts_page = ContactsSteps(self.driver)

        contacts_page.click_add_phone_button()

    def is_add_phone_popup_open(self) -> bool:
        contacts_page = ContactsSteps(self.driver)

        return contacts_page.is_add_phone_popup_title_visible()

    def is_add_phone_popup_close(self) -> bool:

        contacts_page = ContactsSteps(self.driver)

        return contacts_page.is_add_phone_popup_title_close()

    def is_add_email_popup_open(self) -> bool:

        contacts_page = ContactsSteps(self.driver)

        return contacts_page.is_add_email_popup_title_visible()

    def open_add_email_popup(self) -> None:
        contacts_page = ContactsSteps(self.driver)

        contacts_page.click_add_email_button()

    def add_backup_email(self, email) -> None:

        contacts_page = ContactsSteps(self.driver)

        contacts_page.set_email_input(email)
        contacts_page.submit_email_form_button()

    def delete_email(self) -> None:
        contacts_steps = ContactsSteps(self.driver)

        contacts_steps.click_delete_email_button()
        contacts_steps.submit_delete_email()

    def has_not_backup_email(self) -> bool:
        contacts_steps = ContactsSteps(self.driver)

        return contacts_steps.has_backup_email()

    def send_phone(self, phone) -> None:
        contacts_steps = ContactsSteps(self.driver)

        contacts_steps.set_phone_input(phone)

        contacts_steps.submit_phone_form_button()

    def is_phone_error(self) -> bool:
        contacts_steps = ContactsSteps(self.driver)

        return not (contacts_steps.get_phone_input_error() is None)

    def close_phone_popup(self) -> None:
        contacts_steps = ContactsSteps(self.driver)
        contacts_steps.click_close_popup_button()

    def cancel_phone_popup(self) -> None:
        contacts_steps = ContactsSteps(self.driver)
        contacts_steps.click_cancel_popup_button()

