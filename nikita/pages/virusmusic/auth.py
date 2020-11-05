import os

from nikita.pages.virusmusic.default import Page
from nikita.components.virusmusic.auth_form import AuthForm
from nikita.utils import wait_for_element_by_selector, wait_for_url
from nikita.constants import VIRUSMUSIC_BASE_URL

class AuthPage(Page):
    PATH = '/login'
    FORM = 'form.l-form.l-card'
    NAVBAR_LOGIN = '.m-navbar-name'

    def auth(self):
        self.open()
        form = AuthForm(self.driver)
        wait_for_element_by_selector(self.driver, self.FORM)
        form.set_login(os.environ['LOGIN'])
        form.set_password(os.environ['PASSWORD'])
        form.submit()
        wait_for_url(self.driver, VIRUSMUSIC_BASE_URL)

    def get_navbar_login(self):
        return wait_for_element_by_selector(self.driver, self.NAVBAR_LOGIN).get_attribute('innerText')
