from selenium.webdriver.support.wait import WebDriverWait

from tests.components.component import Component


class Basket(Component):
    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: is_shown(d)
        )

    def inc_guest_num(self):
        guest_inc_button(self.driver).click()

    def dec_guest_num(self):
        guest_dec_button(self.driver).click()

    def prod_num(self):
        return sum(list(product_quantities(self.driver)))

    def guest_num(self):
        return int(
            guest_input(self.driver).get_attribute('value')
        )

    def add_product(self, prod_numeral):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: len(products(self.driver)) > prod_numeral
        )
        product_inc_button(
            products(self.driver)[prod_numeral]
        ).click()

    def del_product(self, prod_numeral):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: len(products(self.driver)) > prod_numeral
        )
        product_dec_button(
            products(self.driver)[prod_numeral]
        ).click()

    def is_shown(self):
        return is_shown(self.driver)


def is_shown(driver):
    return guest_input(driver).is_displayed() and\
           title(driver).is_displayed()


def checkout(driver):
    return driver.find_element_by_css_selector(
        'a#order-checkout__href'
    )


def guest_input(driver):
    return driver.find_element_by_css_selector(
        'input#person-input__number-input[class="person-input__input input"]'
    )


def title(driver):
    return driver.find_element_by_css_selector(
        '.order__title'
    )


def guest_inc_button(driver):
    return driver.find_element_by_css_selector(
        'button#person-input__plus-button'
    )


def guest_dec_button(driver):
    return driver.find_element_by_css_selector(
        'button#person-input__minus-button'
    )


def products(driver):
    return driver.find_elements_by_css_selector(
        'li.basket__list-item'
    )


def product_quant(product):
    return int(
        product.find_element_by_css_selector(
            'input[class^="number-input__input-vertical"]'
        ).get_attribute('value')
    )


def product_quantities(driver):
    return map(product_quant, products(driver))


def product_inc_button(product):
    return product.find_element_by_css_selector(
        'button[class^="number-input__plus-button-vertical"]'
    )


def product_dec_button(product):
    return product.find_element_by_css_selector(
        'button[class^="number-input__minus-button-vertical"]'
    )