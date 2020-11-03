from .base import Page
from components.features_form import FeaturesForm
from components.contacts_form import ContactsForm


class FeaturesPage(Page):

    def __init__(self, driver):
        super(FeaturesPage, self).__init__(driver)

        self.form = FeaturesForm(self.driver)

    def compose(self, email):
        self.form.click_dropdown(email)
        self.form.click_compose()

    def create_event(self, email):
        self.form.click_dropdown(email)
        self.form.click_create_event()

    def compose_button_exists(self, email):
        self.form.click_dropdown(email)
        return self.form.compose_button_exists()

    def create_event_button_exists(self, email):
        self.form.click_dropdown(email)
        return self.form.create_event_button_exists()
