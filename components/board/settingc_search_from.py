from selenium.webdriver.support.ui import WebDriverWait
from base_classes.component import Component


class SearchForm(Component):
    CONTAINER = '//div[contains(@class, "search-form")]'
    SEARCH_INPUT = '//input[@id = "js-searchMembersInput"]'
    SEARCH_RESULTS = '//div[@class = "search-result"]'
    INVITE_BUTTON = '//div[contains(@class, "js-addNewMember")]'

    def set_input(self, value):
        search_input = self.driver.find_element_by_xpath(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(value)

    def wait_for_search_results(self):
        WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: len(d.find_elements_by_xpath(self.INVITE_BUTTON)) > 0
        )

    def wait_for_closed(self):
        WebDriverWait(self.driver, 5).until_not(
            lambda d: d.find_element_by_xpath(self.CONTAINER).is_displayed()
        )

    def add_to_board(self, number):
        self.driver.find_elements_by_xpath(self.INVITE_BUTTON)[number].click()
        self.wait_for_closed()
