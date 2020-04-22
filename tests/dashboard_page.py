from selenium.webdriver.support.wait import WebDriverWait

from .general import Page, Component


class DashboardPage(Page):
    PATH = '/dashboard'

    @property
    def dashboard(self):
        return Dashboard(self.driver)


class Dashboard(Component):
    TITLE = '//div[@class="page-header"]'
    USERNAME = '//div[@class="d-account-card"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )
