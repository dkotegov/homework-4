from testutils import Page
from .components import SignInFrom


class AccountPage(Page):
    base_url = 'https://account.mail.ru'
    path = 'login'

    class Actions:
        @staticmethod
        def sign_in(form: SignInFrom, username, password):
            form.fill_login(username)
            form.next()
            form.fill_password(password)
            form.submit()
            form.get_user_email()

    @property
    def form(self):
        return SignInFrom(self.driver)
