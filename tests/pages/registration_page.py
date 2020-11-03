from tests.pages.page import Page
from tests.pages.auth_page import AuthPage
from tests.components.profile_form import ProfileForm
from tests.components.registration_form import RegistrationForm

from selenium.webdriver.support.ui import WebDriverWait


class RegistrationPage(Page):
    REGISTER_CONTAINER = '//div[@class=" signup-field"]'
    PATH = 'me'

    def open(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.wait_open()

        auth_page.auth_form.registration()

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d:
            d.find_element_by_xpath(self.REGISTER_CONTAINER).is_displayed()
        )

    @property
    def registration_form(self):
        return RegistrationForm(self.driver)