from base_element import BaseElement

class AuthForm(BaseElement):
    SUBMIT_BUTTON = '//input[contains(@data-l, "sign_in")]'
    PASSWORD_INPUT = '//input[contains(@name, "st.password")]'
    LOGIN_INPUT = '//input[contains(@name, "st.email")]'

    def get_submit_button(self):
        return self.get_button_by_xpath(self.SUBMIT_BUTTON)
    def get_password_input(self):
        return self.get_field_by_xpath(self.PASSWORD_INPUT)
    def get_login_input(self):
        return self.get_field_by_xpath(self.LOGIN_INPUT)

