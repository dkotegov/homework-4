from nikita.utils import wait_for_element_by_selector
from nikita.components.default import Component

class AuthForm(Component):
    LOGIN = 'input#login'
    PASSWORD = 'input#password'
    SUBMIT = 'button#submit-login'

    def set_login(self, login):
        wait_for_element_by_selector(self.driver, self.LOGIN).send_keys(login)

    def set_password(self, password):
        wait_for_element_by_selector(self.driver, self.PASSWORD).send_keys(password)

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT).click()
