from testutils import Page
from .components import SignInForm


class AuthPage(Page):
    base_url = "https://softree.group"
    path = "signin"

    class Actions:
        @staticmethod
        def sign_in(form: SignInForm, username, password):
            form.go_to_signin()
            form.fill_login(username)
            form.fill_password(password)
            form.submit()

    @property
    def form(self):
        return SignInForm(self.driver)
