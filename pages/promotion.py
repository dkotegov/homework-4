from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page, Component


class PromotionForm(Component):
    ERROR = "#promotion-error"

    BASE_TARIFF = "#base-tariff"
    IMPROVED_TARIFF = "#improved-tariff"
    ADVANCED_TARIFF = "#advanced-tariff"
    NO_TARIFF = "#block-no-tariff"

    BLOCK_BASE = "#block-base-tariff"
    BLOCK_IMPROVED = "#block-improved-tariff"
    BLOCK_ADVANCED = "#block-advanced-tariff"

    CHECKED_TARIFF = "tariffs-block_checked"
    UNCHECKED_TARIFF = "tariffs-block_unchecked"

    SUBMIT = ".promotion-button__purchase"

    def enter_submit(self):
        self.helpers.click_element(self.SUBMIT)

    def is_submit_error(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.ERROR)))
        return self.helpers.is_contains(self.ERROR)

    def enter_base_tariff(self):
        self.helpers.click_element(self.BASE_TARIFF)

    def enter_no_tariff(self):
        self.helpers.click_element(self.NO_TARIFF)

    def enter_improved_tariff(self):
        self.helpers.click_element(self.IMPROVED_TARIFF)

    def enter_advanced_tariff(self):
        self.helpers.click_element(self.ADVANCED_TARIFF)

    def is_base_checked(self):
        return self.helpers.is_contains_class(self.BLOCK_BASE, self.CHECKED_TARIFF)

    def is_improved_checked(self):
        return self.helpers.is_contains_class(self.BLOCK_IMPROVED, self.CHECKED_TARIFF)

    def is_advanced_checked(self):
        return self.helpers.is_contains_class(self.BLOCK_ADVANCED, self.CHECKED_TARIFF)

    def is_base_unchecked(self):
        return self.helpers.is_contains_class(self.BLOCK_BASE, self.UNCHECKED_TARIFF)

    def is_improved_unchecked(self):
        return self.helpers.is_contains_class(self.BLOCK_IMPROVED, self.UNCHECKED_TARIFF)

    def is_advanced_unchecked(self):
        return self.helpers.is_contains_class(self.BLOCK_ADVANCED, self.UNCHECKED_TARIFF)


class PromotionPage(Page):
    PATH = "/promotion"

    PAGE = ".promotion"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def send_state(self, product_id):
        script = "window.history.pushState({" + "\"id\": \"{}\"".format(product_id) + "}, \"\", " + "\"{}\")".format(self.PATH)
        self.driver.execute_script(script)

    @property
    def form(self):
        return PromotionForm(self.driver)
