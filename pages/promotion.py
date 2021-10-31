from pages.default_page import DefaultPage


class PromotionPage(DefaultPage):
    PATH = "promotion"

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

    PURCHASE = "promotion-button__purchase"

    TYPE = "#promotion-type"

    def enter_purchase(self):
        self.__click_button__(self.PURCHASE)

    def get_purchase_error(self):
        return self.__get_element__(self.ERROR).text

    def enter_base_tariff(self):
        self.__click_button__(self.BASE_TARIFF)

    def enter_no_tariff(self):
        self.__click_button__(self.NO_TARIFF)

    def enter_improved_tariff(self):
        self.__click_button__(self.IMPROVED_TARIFF)

    def enter_advanced_tariff(self):
        self.__click_button__(self.ADVANCED_TARIFF)

    def is_base_checked(self):
        return self.__element_contains_class__(self.BLOCK_BASE, self.CHECKED_TARIFF)

    def is_improved_checked(self):
        return self.__element_contains_class__(self.BLOCK_IMPROVED, self.CHECKED_TARIFF)

    def is_advanced_checked(self):
        return self.__element_contains_class__(self.BLOCK_ADVANCED, self.CHECKED_TARIFF)

    def is_base_unchecked(self):
        return self.__element_contains_class__(self.BLOCK_BASE, self.UNCHECKED_TARIFF)

    def is_improved_unchecked(self):
        return self.__element_contains_class__(self.BLOCK_IMPROVED, self.UNCHECKED_TARIFF)

    def is_advanced_unchecked(self):
        return self.__element_contains_class__(self.BLOCK_ADVANCED, self.UNCHECKED_TARIFF)

