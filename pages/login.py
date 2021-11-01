from pages.default import Page
from components.login_form import LoginForm

from utils import wait_for_url, wait_for_element_by_selector


class LoginPage(Page):
    PATH = "login/"
    TITLE_OF_PAGE = ".content__title"

    def auth(self):
        self.open()
        form = LoginForm(self.driver)
        form.set_login('user@user.ru')
        form.set_password('password')
        form.submit()
        wait_for_url(self.driver, self.BASE_URL)

    def get_title_of_page(self):
        return wait_for_element_by_selector(self.driver, self.TITLE_OF_PAGE).text
