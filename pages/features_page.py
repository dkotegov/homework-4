from .base import Page
from components.features_form import FeaturesForm
from components.groups_form import GroupsForm


class FeaturesPage(Page):

    def __init__(self, driver):
        super(FeaturesPage, self).__init__(driver)

        self.features = FeaturesForm(self.driver)
        self.groups = GroupsForm(self.driver)

    def compose(self, email):
        self.features.click_dropdown(email)
        self.features.click_compose()

    def create_event(self, email):
        self.features.click_dropdown(email)
        self.features.click_create_event()

    def compose_button_exists(self, email):
        self.features.click_dropdown(email)
        return self.features.compose_button_exists()

    def create_event_button_exists(self, email):
        self.features.click_dropdown(email)
        return self.features.create_event_button_exists()

    def import_contacts(self, path, group_name):
        self.groups.click_dropdown()
        self.features.click_import()
        if path != u'':
            self.features.upload_file(path)
        if group_name != u'':
            self.features.input_import_group_name(group_name)
        self.features.click_submit()

    def open_import_popup(self):
        self.groups.click_dropdown()
        self.features.click_import()

    def close_import_popup(self):
        self.features.click_cancel()

    def import_error_exists(self):
        return self.features.import_error_exists()

    def input_error_exists(self):
        return self.features.input_error_exists()

    def import_popup_exists(self):
        return self.features.import_popup_exists()

    def export_all_contacts(self):
        self.groups.click_dropdown()
        self.features.click_export()
        self.features.click_submit()

    def export_contacts_from_groups(self, ids, format='apple'):
        self.groups.click_dropdown()
        self.features.click_export()
        if format == 'outlook':
            self.features.click_outlook_radio()
        elif format == 'google':
            self.features.click_google_radio()
        self.features.click_group_select()
        self.features.click_group_options(ids)
        self.features.click_submit()

    def open_export_popup(self):
        self.groups.click_dropdown()
        self.features.click_export()

    def close_export_popup(self):
        self.features.click_cancel()

    def export_popup_exists(self):
        return self.features.export_popup_exists()

    def get_attendee_emails(self):
        return self.features.get_attendee_emails()
