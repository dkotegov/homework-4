import utils
from components.default import Component
from selenium.webdriver.common.by import By


class SearchPopup(Component):
    OPEN = '.js-search-popup'
    CLOSE = '.popup__close'
    POPUP = '.search-popup__popup'
    SEARCH = '#search'
    SEARCH_RESULT = '.search-results__body'
    SEARCH_ITEM = '.search-results__body_item'
    TITLE_SEARCH_ITEM = '.body_item__title'

    def open(self):
        utils.wait_for_element_by_selector(self.driver, self.OPEN).click()

    def close(self):
        utils.wait_for_element_by_selector(self.driver, self.CLOSE).click()

    def search(self, search_string):
        search = utils.wait_for_element_by_selector(self.driver, self.SEARCH)
        search.clear()
        for letter in search_string:
            search.send_keys(letter)

    def click_on_founded_item(self):
        utils.wait_for_element_by_selector(self.driver, self.TITLE_SEARCH_ITEM).click()

    def click_on_named_founded_item(self, text):
        utils.wait_for_element_by(self.driver, text, By.LINK_TEXT).click()

    def count_found_items(self):
        return len(utils.wait_for_element_by_selector(self.driver, self.SEARCH_RESULT)
                   .find_elements_by_css_selector(self.SEARCH_ITEM))

    def is_visible(self):
        try:
            utils.wait_for_element_by_selector(self.driver, self.POPUP)
            return True
        except:
            return False
