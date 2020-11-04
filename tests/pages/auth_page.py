from tests.pages.page import Page
from tests.components.login_form import LoginForm

from selenium.webdriver.support.ui import WebDriverWait


class AuthPage(Page):
    LOGIN_CONTAINER = '//div[@class=" login-field"]'
    PATH = 'me'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d:
            d.find_element_by_xpath(self.LOGIN_CONTAINER).is_displayed()
        )

    @property
    def auth_form(self):
        return LoginForm(self.driver)

    def auth(self, phone, password):
        login_form = LoginForm(self.driver)

        login_form.wait_visible()
        login_form.set_phone(phone)
        login_form.set_password(password)
        login_form.submit()
