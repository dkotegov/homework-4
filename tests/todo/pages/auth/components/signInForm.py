from testutils import Component
from selenium.webdriver.common.by import By


class SignInFrom(Component):
    container = '[data-test-id=login-app-ready]'

    class Selectors:
        login = 'input[name="username"]'
        password = 'input[name="password"]'
        next_button = '[data-test-id="next-button"]'
        submit_button = '[data-test-id="submit-button"]'
        user_email_header = '#PH_user-email'

    def get_user_email(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.user_email_header)
        return self.driver.find_element_by_css_selector(self.Selectors.user_email_header).text

    def fill_login(self, username):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.login, username)

    def next(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.next_button)
        self.driver.find_element_by_css_selector(self.Selectors.next_button).click()

    def fill_password(self, password):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, password)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit_button)
        self.driver.find_element_by_css_selector(self.Selectors.submit_button).click()
