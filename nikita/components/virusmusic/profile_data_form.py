from nikita.utils import wait_for_element_by_selector, wait_for_element_value
from nikita.components.default import Component

class ProfileDataForm(Component):
    NAME = 'input#name'
    EMAIL = 'input#email'
    SUBMIT = 'button#submit-setting-changes-data'

    def set_name(self, name):
        nameInput = wait_for_element_by_selector(self.driver, self.NAME)
        nameInput.clear()
        nameInput.send_keys(name)

    def get_name_value(self):
        wait_for_element_value(self.driver, self.NAME)
        return self.driver.find_element_by_css_selector(self.NAME).get_attribute('value')

    def set_email(self, email):
        emailInput = wait_for_element_by_selector(self.driver, self.EMAIL)
        emailInput.clear()
        emailInput.send_keys(email)

    def get_email_value(self):
        wait_for_element_value(self.driver, self.EMAIL)
        return self.driver.find_element_by_css_selector(self.EMAIL).get_attribute('value')

    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT).click()
