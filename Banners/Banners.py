from Base import Component


class Banners(Component):
    BANNER = '//div[@data-qa-modal]'
    MINI_BANNER = '//div[@class="PromoTooltip__root--2vPmD"]'
    BUY_CLOUD_BANNER = '//div[@class="b-tooltip__content"]'
    CLOSE_MINI_BANNER_BUTTON = '//div[@class="PromoTooltip__close--3zFr1 PromoTooltip__closeLight--JBMkK"]'
    CLOSE_BANNER_BUTTON = '//*[local-name() = "svg" and @class="Dialog__close--1rKyk"]'
    CLOSE_BUY_CLOUD_BANNER = '//div[@class="b-panel__close__icon"]'

    def close_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_BANNER_BUTTON).click()

    def close_mini_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.MINI_BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_MINI_BANNER_BUTTON).click()

    def close_buy_cloud_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BUY_CLOUD_BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.BUY_CLOUD_BANNER).click()