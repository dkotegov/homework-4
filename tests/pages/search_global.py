from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.config import onload


class GlobalSearchPage(Page):
    # PATH = '/search/{0}&{1}'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="search-page"]')
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def search_form(self):
        return HeaderSearchForm(self.driver)

    @property
    def result_form(self):
        return SearchResultsForm(self.driver)


class HeaderSearchForm(FormComponent):
    search_line = '#searchtext'
    search_type = '#style-select'
    search_form = '#headerSearch'

    @onload
    def search(self, type, query):
        self.fill_input(self.find_element(By.CSS_SELECTOR, self.search_line), query)
        Select(self.find_element(By.CSS_SELECTOR, self.search_type)).select_by_value(type)
        self.find_element(By.CSS_SELECTOR, self.search_form).submit()

    def wait_for_load(self):
        self.wait_for_presence(By.CSS_SELECTOR,  self.search_line)


class SearchResultsForm(FormComponent):
    container = '.search-page__flex-container'
    elements_names = '.user-for-search__username'
    element = '.pin-for-index-view'
    elements_name_tag = '.pin-for-index__content'
    error_message = '.search-page__error-message'

    def wait_for_load(self, timeout=5):
        self.wait_for_presence(By.CSS_SELECTOR, self.container, timeout)

    def get_search_results(self):
        self.wait_for_presence(By.CSS_SELECTOR, self.elements_names)
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.elements_names)
        return [elem.text for elem in elements]

    def get_search_results_raw(self):
        self.wait_for_presence(By.CSS_SELECTOR, self.element)
        return self.find_elements(By.CSS_SELECTOR, self.element)

    def click_pin(self, pin):
        pin_clickable = pin.find_element(By.CSS_SELECTOR, self.elements_name_tag)
        pin_clickable.click()

    @onload
    def check_search_results(self, after_click_func):
        results = self.get_search_results_raw()
        for i in range(len(results)):
            s = self.get_search_results_raw()
            if len(s) <= i:
                continue
            result = s[i]
            self.click_pin(result)
            after_click_func()
            self.driver.back()
            self.driver.refresh()

    def wait_for_error(self, timeout=5):
        try:
            self.wait_for_presence(By.CSS_SELECTOR, self.error_message, timeout=timeout)
            return True
        except:
            return False
