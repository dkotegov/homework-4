from components.page import Page
from components.about_form import AboutForm


class AboutPage(Page):

    def about_form(self):
        return AboutForm(self.driver)