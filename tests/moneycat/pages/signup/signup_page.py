from testutils import Page
from .components import SignUpForm


class SignUpPage(Page):
    base_url = "https://softree.group"
    path = "signup"

    class Actions:
        @staticmethod
        def sign_up(form: SignUpForm, username, password1, password2):
            form.fill_login(username)
            form.fill_password1(password1)
            form.fill_password2(password2)
            form.submit()

        def go_to_sign_in(form: SignUpForm):
            form.click_signin_href()

    @property
    def form(self):
        return SignUpForm(self.driver)