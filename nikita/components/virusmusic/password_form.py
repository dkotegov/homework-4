from nikita.utils import wait_for_element_by_selector
from nikita.components.default import Component

class PasswordForm(Component):
    NEW_PASSWORD = 'input#newPassword'
    NEW_PASSWORD_CONFIRM = 'input#newPasswordConfirm'
    PASSWORD = 'input#password'
    SUBMIT = 'button#submit-setting-changes-pass'

    def set_new_password(self, password):
        newPasswordInput = wait_for_element_by_selector(self.driver, self.NEW_PASSWORD)
        newPasswordInput.clear()
        newPasswordInput.send_keys(password)

    def set_new_password_confirm(self, password):
        newPasswordConfirmInput = wait_for_element_by_selector(self.driver, self.NEW_PASSWORD_CONFIRM)
        newPasswordConfirmInput.clear()
        newPasswordConfirmInput.send_keys(password)

    def set_password(self, password):
        passwordInput =  wait_for_element_by_selector(self.driver, self.PASSWORD)
        passwordInput.clear()
        passwordInput.send_keys(password)

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT).click()
