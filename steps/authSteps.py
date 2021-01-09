from .BaseSteps import *


class AuthForm(BaseSteps):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    SUBMIT_BUTTON = '//button[@data-test-id="submit-button"]'

    def set_login(self, login):
        self.fill_input_without_submitting(self.LOGIN, login)

    def set_password(self, password):
        self.fill_input_without_submitting(self.PASSWORD, password)

    def submit(self):
        self.wait_to_be_clickable_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_for_cookie(self):
        self.wait_for_url("https://e.mail.ru/inbox/?afterReload=1")

    def click_next(self):
        self.wait_until_and_get_elem_by_xpath(self.NEXT_BUTTON).click()
