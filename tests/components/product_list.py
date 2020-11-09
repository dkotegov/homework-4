from tests.components.component import Component


class ProductList(Component):
    def wait_visible(self):
        pass

    def add_product(self, prod_numeral):
        product_add_button(
            products(self.driver)[prod_numeral]
        ).click()

    def del_product(self, prod_numeral):
        product_del_button(
            products(self.driver)[prod_numeral]
        ).click()


def prod_container(driver):
    return driver.find_element_by_css_selector(
        'div.restaurant-view__product-list'
    )


def products(driver):
    return driver.find_elements_by_css_selector(
        'div.product-card__container'
    )


def product_add_button(product):
    primary_add = product.find_element_by_css_selector(
        'button[class="product-card-button button"]'
    )

    if primary_add.get_attribute('display') == 'none':
        return product.find_element_by_css_selector(
            'button[class^="number-input__plus-button-horizontal"'
        )
    else:
        return primary_add


def product_del_button(product):
    primary_add = product.find_element_by_css_selector(
        'button[class="product-card-button button"]'
    )
    display = primary_add.get_attribute('display')
    if display == 'none' or display is None:
        return product.find_element_by_css_selector(
            'button[class^="number-input__minus-button-horizontal"'
        )
    else:
        raise Exception("no such product selected")
