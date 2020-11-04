from tests.pages.page import Page
from tests.components.login_form import LoginForm
from tests.components.main_form import MainForm
from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class MainPage(Page):
    NAVBAR = '//nav[contains(@class, "iconed-header__icon-bar")]'
    REST_LIST = '//div[@class="main-view__restaurant-list"]'
    PATH = ''

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: 
                d.find_element_by_xpath(self.NAVBAR).is_displayed() and 
                d.find_element_by_xpath(self.REST_LIST).is_displayed()
        )
    
    @property
    def main_form(self):
        return MainForm(self.driver)

    def auth(self, phone, password):
        login_form = LoginForm(self.driver)

        login_form.open_form()
        login_form.wait_visible()
        login_form.set_phone(phone)
        login_form.set_password(password)
        login_form.submit()
        login_form.wait_close()
