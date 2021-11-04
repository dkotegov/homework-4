from components.default import Component

from utils import wait_for_element_by_selector


class ProfileForm(Component):
    EMPTY_STR = ''
    LOGIN = '#login'
    EMAIL = '#email'
    SUBMIT = '.input-wrapper__button'

    def get_login(self):
        return wait_for_element_by_selector(self.driver, self.LOGIN).get_attribute('value')

    def get_email(self):
        return wait_for_element_by_selector(self.driver, self.EMAIL).get_attribute('value')

    def set_login(self, login):
        login_input = wait_for_element_by_selector(self.driver, self.LOGIN)
        login_input.clear()
        login_input.send_keys(login)

    def set_email(self, email):
        email_input = wait_for_element_by_selector(self.driver, self.EMAIL)
        email_input.clear()
        email_input.send_keys(email)

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT).click()
        wait_for_element_by_selector(self.driver, self.SUBMIT)
