from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class PinPage(Page):
    PATH = ''

    @property
    def pin_modal(self):
        return PinModal(self.driver)


class PinModal(Component):

    PIN_AUTHOR = '//*[@class="nick"]'

    def get_author(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PIN_AUTHOR)
        )
        return self.driver.find_element_by_xpath(self.PIN_AUTHOR).get_attribute('innerText')
