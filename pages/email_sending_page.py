from components.email_sending_form import EmailSendingForm
from pages.page import Page


class EmailSendingPage(Page):
    PATH = ''

    @property
    def form(self):
        return EmailSendingForm(self.driver)
