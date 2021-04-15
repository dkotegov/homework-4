import testutils
from selenium.webdriver.common.by import By


class HeaderForm(testutils.Component):
    class Selectors:
        logo = '[class=header__logo]'
        account = '#account'
        avatar = '[class=header__control-avatar]'
        info_dropdown_menu = '[class=drop-down-menu__info]'
        settings_dropdown_menu = '#drop-down-settings-btn'
        exit_dropdown_menu = '#drop-down-exit-btn'
        bag = '#bag'
        history = '#history'
        catalog = '#catalog'
        auth_container = '.modal__title'
        settings_container = '.settings.container'
        bag_container = '.bag.container'
        history_container = '.history.container'

    def click_logo(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.logo)
        self.driver.find_element_by_css_selector(self.Selectors.logo).click()

    def click_catalog(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.catalog)
        self.driver.find_element_by_css_selector(self.Selectors.catalog).click()

    def click_account(self) -> bool:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.account)
        self.driver.find_element_by_css_selector(self.Selectors.account).click()
        return self.driver.find_element_by_css_selector(self.Selectors.settings_container).is_displayed()

    def click_avatar(self) -> bool:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.avatar)
        self.driver.find_element_by_css_selector(self.Selectors.avatar).click()
        return self.driver.find_element_by_css_selector(self.Selectors.info_dropdown_menu).is_displayed()

    def click_settings_in_drop_down_menu(self) -> bool:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.settings_dropdown_menu)
        self.driver.find_element_by_css_selector(self.Selectors.settings_dropdown_menu).click()
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.settings_container)
        return self.driver.find_element_by_css_selector(self.Selectors.settings_container).is_displayed()

    def click_exit_in_drop_down_menu(self) -> bool:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.exit_dropdown_menu)
        self.driver.find_element_by_css_selector(self.Selectors.exit_dropdown_menu).click()
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.auth_container)
        return self.driver.find_element_by_css_selector(self.Selectors.auth_container).is_displayed()

    def click_bag(self) -> bool:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.bag)
        self.driver.find_element_by_css_selector(self.Selectors.bag).click()
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.bag_container)
        return self.driver.find_element_by_css_selector(self.Selectors.bag_container).is_displayed()

    def click_history(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.history)
        self.driver.find_element_by_css_selector(self.Selectors.history).click()
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.history_container)
        return self.driver.find_element_by_css_selector(self.Selectors.history_container).is_displayed()
