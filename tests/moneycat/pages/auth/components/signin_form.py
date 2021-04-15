from testutils import Component
from selenium.webdriver.common.by import By


class SignInForm(Component):
    container = '[data-test-id=modal]'

    class Selectors:
        login = 'input[type="email"]'
        password = 'input[type="password"]'
        submit_button = 'input[type="submit"]'
        account_header = 'p[id="account"]'
        href_to_signin = 'a[class="signin-link"]'
        error_message = 'p[class="field__error"]'
        href_to_signup = 'a[class="signup-link"]'
        registration_title = '[class="modal__title"]'

    def go_to_signin(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signin).click()

    def get_account_header(self) -> str:
        return self._wait_clickable(By.CSS_SELECTOR, self.Selectors.account_header).text

    def get_error_message(self) -> str:
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.error_message).text

    def fill_login(self, username):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.login, username)

    def fill_password(self, password):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, password)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit_button).click()

    def click_signup_href(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signup).click()

    def get_registration_title(self):
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.registration_title).text
