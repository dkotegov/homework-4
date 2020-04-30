from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class PinDetailsPage(Page):
    PATH = '/pin/{0}'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="viewpin-page"]')
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def form(self):
        return PinForm(self.driver)


class PinForm(FormComponent):
    title = '.viewpin-block__right-column__title'
    tag = '.viewpin-block__right-column__context'

    def get_title(self):
        return self.find_element(By.CSS_SELECTOR, self.title).text

    def get_tag(self):
        return self.find_element(By.CSS_SELECTOR, self.tag).text

    def wait_for_load(self):
        self.wait_for_presence(By.CSS_SELECTOR, self.title)
