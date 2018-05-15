from components.base_component import BaseComponent


class AuthForm(BaseComponent):
    EMAIL_INPUT = "//input[@id='field_email']"
    PASSWORD_INPUT = "//input[@id='field_password']"
    SUBMIT_BUTTON = "//input[@class='button-pro __wide']"

    def get_login(self):
        return self.driver.find_element_by_xpath(self.EMAIL_INPUT)

    def get_password(self):
        return self.driver.find_element_by_xpath(self.PASSWORD_INPUT)

    def submit(self):
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON)