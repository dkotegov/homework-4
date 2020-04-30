from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class GeneralPage(Page):
    PATH = '/index/new'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="index-page:new"]')
    }

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form(self):
        return PinListForm(self.driver)


class PinListForm(FormComponent):
    element = '.pin-for-index-view'
    element_title = '.pin-for-index__content'

    def click_first_pin(self):
        elem = self.find_element(By.CSS_SELECTOR, self.element)
        pin_clickable = elem.find_element(By.CSS_SELECTOR, self.element_title)
        title = pin_clickable.text
        url = elem.find_element_by_tag_name("a").get_attribute("href")

        pin_clickable.click()
        return title, url


