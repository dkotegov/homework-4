from components.default import Component

from utils import wait_for_element_by_selector


class SignupForm(Component):
    EMPTY_STR = ''
    LOGIN = '#login'
    LOGIN_ERROR = '#loginError'
    EMAIL = '#email'
    EMAIL_ERROR = '#emailError'
    PASSWORD = '#password'
    PASSWORD_ERROR = '#passwordError'
    CONFIRM_PASSWORD = '#confirmPassword'
    CONFIRM_PASSWORD_ERROR = '#confirmPasswordError'
    SUBMIT = '.form-content__button'

    def get_login_error(self):
        return wait_for_element_by_selector(self.driver, self.LOGIN_ERROR).text

    def get_email_error(self):
        return wait_for_element_by_selector(self.driver, self.EMAIL_ERROR).text

    def get_password_error(self):
        return wait_for_element_by_selector(self.driver, self.PASSWORD_ERROR).text

    def get_confirm_password_error(self):
        return wait_for_element_by_selector(self.driver, self.CONFIRM_PASSWORD_ERROR).text

    def get_login(self):
        return wait_for_element_by_selector(self.driver, self.LOGIN).get_attribute('value')

    def get_email(self):
        return wait_for_element_by_selector(self.driver, self.EMAIL).get_attribute('value')

    def get_password(self):
        return wait_for_element_by_selector(self.driver, self.PASSWORD).get_attribute('value')

    def get_confirm_password(self):
        return wait_for_element_by_selector(self.driver, self.CONFIRM_PASSWORD).get_attribute('value')

    def set_login(self, login):
        login_input = wait_for_element_by_selector(self.driver, self.LOGIN)
        login_input.clear()
        login_input.send_keys(login)

    def set_email(self, email):
        email_input = wait_for_element_by_selector(self.driver, self.EMAIL)
        email_input.clear()
        email_input.send_keys(email)

    def set_password(self, password):
        password_input = wait_for_element_by_selector(self.driver, self.PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

    def set_confirm_password(self, password):
        password_input = wait_for_element_by_selector(self.driver, self.CONFIRM_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT).click()
