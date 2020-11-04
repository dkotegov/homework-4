from tests.pages.page import Page
from tests.components.login_form import LoginForm
from tests.components.profile_form import ProfileForm

from selenium.webdriver.support.ui import WebDriverWait


class ProfilePage(Page):
    LOGIN_CONTAINER = '//div[@class="profile-view__profile-area"]'
    PATH = 'me'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_CONTAINER)
        )

    @property
    def profile_form(self):
        return ProfileForm(self.driver)