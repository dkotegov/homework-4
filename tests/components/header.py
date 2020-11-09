from selenium.webdriver.support.wait import WebDriverWait

from tests.components.component import Component


class Header(Component):
    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: icons(d).is_displayed()
        )

    def show_basket(self):
        basket_icon(self.driver).click()


def logo(driver):
    return driver.find_element_by_css_selector(
        '#a[class="header__logo href"]'
    )


def address_input(driver):
    return driver.find_element_by_css_selector(
        '.header__search-field'
    )


def icons(driver):
    return driver.find_element_by_css_selector(
        'nav[class="icon-bar iconed-header__icon-bar"]'
    )


def basket_icon(driver):
    return driver.find_element_by_css_selector(
        'img#icon-bar-basket-href[class="icon-bar__basket-image icon"]'
    )