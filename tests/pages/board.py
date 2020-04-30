from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class BoardPage(Page):
    PATH = '/board/{0}'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="board-page"]')
    }

    def __init__(self, driver, board_id):
        Page.__init__(self, driver)
        self.open(board_id)

    @property
    def form(self):
        return BoardForm(self.driver)


class BoardForm(FormComponent):
    pins = '//div[@class="pin-for-user-view"]'
    section_name = '//div[@id="board-page"]'

    def find_pin_id_by_pin_name(self, name):
        pins = self.driver.find_elements_by_xpath(self.pins)
        for pin in pins:
            if pin.text == name:
                href = pin.find_element(by=By.CLASS_NAME, value="pin-for-user-view__content").get_attribute("href")
                return href[28:]

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)


