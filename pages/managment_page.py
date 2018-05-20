from pages.page import Page
from pages.settings_components import ManagmentForm, WhoCanLeaveComments


class ManagmentPage(Page):

    @property
    def form(self):
        return ManagmentForm(self.driver)

    def generate_access_key(self):
        return self.form.generate_api_key()

    def hide_obscene_language(self):
        form = self.form
        form.hide_obscene()
        form.save_settings()

    def hide_photo_section(self):
        form = self.form
        form.hide_photo_section()
        form.save_settings()

    def hide_video_section(self):
        form = self.form
        form.hide_video_section()
        form.save_settings()

    def forbid_leave_comments(self, who: WhoCanLeaveComments):
        form = self.form
        form.forbid_leave_comments(who)
        form.save_settings()
