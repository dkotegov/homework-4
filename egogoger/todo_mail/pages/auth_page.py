from egogoger.utils import wait_for_element_by_selector, set_input
from egogoger.default_page import DefaultPage, Component


class AuthPage(DefaultPage):
    page = None
    CONTAINER = 'div.c0113'
    EMAIL_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    NEXT_BUTTON = 'button[data-test-id="next-button"]'
    SUBMIT_BUTTON = 'button[data-test-id="submit-button"]'

    def __init__(self, driver, path='https://account.mail.ru/'):
        super().__init__(driver, path)

    # METHODS
    def next(self):
        self.driver.find_element_by_css_selector(self.NEXT_BUTTON).click()

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()

    # CHECKERS
    def check_for_self(self, test):
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        # test.assertEqual(
        #     self.PATH+'login?page=https://todo.mail.ru',
        #     self.driver.current_url)
