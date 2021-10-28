from pages.base_page import BasePage


class SignupPage(BasePage):
    PATH = '/signup'

    AUTH_BTN = 'div.muted > linkbutton'
    SIGNUP_BTN = 'input[type="submit"]'

    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    PASSWORD_CONFIRM_INPUT = 'input[name="passwordConfirm"]'
    EMAIL_INPUT = 'input[name="reserveEmail"]'

    USERNAME_ERROR = '#usernameErrorText'
    PASSWORD_ERROR = '#passwordErrorText'
    PASSWORD_CONFIRM_ERROR = '#passwordConfirmErrorText'
    EMAIL_ERROR = '#reserveEmailErrorText'

    def __init__(self, driver):
        super().__init__(driver, 'div.signup')

    def set_username(self, username):
        self.set_field(self.USERNAME_INPUT, username)

    def set_password(self, password):
        self.set_field(self.PASSWORD_INPUT, password)

    def set_password_confirm(self, password_confirm):
        self.set_field(self.PASSWORD_CONFIRM_INPUT, password_confirm)

    def set_email(self, email):
        self.set_field(self.EMAIL_INPUT, email)

    def get_username_error(self):
        return self.locate_el(self.USERNAME_ERROR).text

    def get_password_error(self):
        return self.locate_el(self.PASSWORD_ERROR).text

    def get_password_confirm_error(self):
        return self.locate_el(self.PASSWORD_CONFIRM_ERROR).text

    def get_email_error(self):
        return self.locate_el(self.EMAIL_ERROR).text

    def click_signup_btn(self):
        self.locate_el(self.SIGNUP_BTN).click()

    def click_auth_btn(self):
        self.locate_el(self.AUTH_BTN).click()
