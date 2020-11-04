from base_classes.page import Page
from components.join_form import JoinForm
from components.boards_form import BoardsForm


class JoinPage(Page):
    PATH = 'join'
    CONTAINER = '//div[@class="auth-form-join"]'

    @property
    def join_form(self):
        return JoinForm(self.driver)

    def join(self, name, surname, login, password, passwordRepeat):
        self.join_form.set_name(name)
        self.join_form.set_surname(surname)
        self.join_form.set_login(login)
        self.join_form.set_password(password)
        self.join_form.set_password_repeat(passwordRepeat)

        self.join_form.submit()

        return BoardsForm(self.driver).is_open
