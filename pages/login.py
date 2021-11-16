import os

import utils
from pages.default import Page
from pages.main import MainPage
from components.login_form import LoginForm


class LoginPage(Page):
    PATH = 'login/'
    TITLE_OF_PAGE = '.content__title'
    SIGNUP_LINK = 'a.have-acc__href'

    EMAIL_ERROR = 'div.error#emailError'
    PASSWORD_ERROR = 'div#passwordError'

    def auth(self):
        self.open()
        form = LoginForm(self.driver)
        form.set_login(os.environ['LOGIN'])
        form.set_password(os.environ['PASSWORD'])
        form.submit()
        main_page = MainPage(self.driver)
        main_page.wait_for_container()

    def auth_with(self, login, password):
        self.open()
        form = LoginForm(self.driver)
        form.set_login(login)
        form.set_password(password)
        form.submit()
        main_page = MainPage(self.driver)

    def get_title_of_page(self):
        return utils.wait_for_element_by_selector(self.driver, self.TITLE_OF_PAGE).text

    def click_on_register(self):
        utils.wait_click_for_element_by_selector(self.driver, self.SIGNUP_LINK)

    def click_login(self):
        form = LoginForm(self.driver)
        form.submit()

    def has_email_error(self):
        utils.wait_for_element_by_selector(self.driver, self.EMAIL_ERROR)
        return True

    def has_password_error(self):
        utils.wait_for_element_by_selector(self.driver, self.PASSWORD_ERROR)
        return True
