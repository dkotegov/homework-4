import testutils
from selenium.webdriver.common.by import By


class CurrencyList(testutils.Component):
    container = '.rates-wrapper'

    class Selectors:
        first_currency_card = '[class=rate-card]'
        last_currency_card = '[class=rate-card]:last-child'

    def is_currency_card_visible(self) -> bool:
        return bool(self.driver.find_element_by_css_selector(self.Selectors.first_currency_card).is_displayed())

    def open_first_currency(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.first_currency_card)
        self.driver.find_element_by_css_selector(self.Selectors.first_currency_card).click()

    def open_last_currency(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.last_currency_card)
        self.driver.find_element_by_css_selector(self.Selectors.last_currency_card).click()
