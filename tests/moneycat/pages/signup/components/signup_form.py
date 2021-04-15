from testutils import Component
from selenium.webdriver.common.by import By


class SignUpForm(Component):
    container = '[data-test-id=modal]'

    class Selectors:
        login = 'input[type="email"]'
        password1 = 'input[name="password1"]'
        password2 = 'input[name="password2"]'
        submit_button = 'input[type="submit"]'
        href_to_signin = 'a[class="signin-link"]'
        error_message = '.field__error'
        registration_title = '[class="modal__title"]'
        account_header = 'p[id="account"]'

    def go_to_signin(self):
        return self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signin).click()

    def get_account_header(self) -> str:
        return self._wait_clickable(By.CSS_SELECTOR, self.Selectors.account_header).text

    def get_error_message(self, num) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.error_message)
        return self.driver.find_elements_by_css_selector(self.Selectors.error_message)[num].text

    def fill_login(self, username):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.login, username)

    def fill_password1(self, password1):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password1, password1)

    def fill_password2(self, password2):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password2, password2)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit_button).click()

    def get_auth_title(self):
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.registration_title).text

    def click_signin_href(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signin).click()
