import os

from selenium.webdriver.common.keys import Keys

from pages.default import DefaultPage, DefaultSteps


class AccountPage(DefaultPage):
    URL = 'https://account.mail.ru'
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    CONTAINER = '[class="scrollable__container"]'
    CONTAINER_PROFILE = '[class="page-content"]'

    def auth(self):
        auth_steps = AccountSteps(self.driver)

        auth_steps.set_login(self.LOGIN)
        auth_steps.set_password(self.PASSWORD)
        auth_steps.waiting_for_visible(self.CONTAINER)

    def auth_main_page(self):
        auth_steps = AccountSteps(self.driver)

        auth_steps.set_login(self.LOGIN)
        auth_steps.set_password(self.PASSWORD)
        self.driver.switch_to.default_content()
        auth_steps.waiting_for_visible(self.CONTAINER_PROFILE)


class AccountSteps(DefaultSteps):
    LOGIN = 'input[name="Login"]'
    PASSWORD = 'input[name="Password"]'

    def set_login(self, login):
        self.waiting_for_visible(self.LOGIN)
        elem = self.driver.find_element_by_css_selector(self.LOGIN)
        elem.send_keys(login)
        elem.send_keys(Keys.RETURN)

    def set_password(self, pwd):
        self.waiting_for_visible(self.PASSWORD)
        elem = self.driver.find_element_by_css_selector(self.PASSWORD)
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

