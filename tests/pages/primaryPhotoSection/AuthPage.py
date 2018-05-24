from tests.Components.AuthPageComponents.AuthForm import AuthForm
from tests.pages.primaryPhotoSection.Page import Page


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)
