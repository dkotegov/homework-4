from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class OrderHistoryPage(Page):
    PATH = 'orders'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: title(d).is_displayed()
        )

    def last_restaurant_name(self):
        return restaurant_name(
            history_cards(self.driver)[-1]
        )

    def last_product_name(self):
        return product_name(
            history_cards(self.driver)[-1]
        )

    def last_product_price(self):
        return product_price(
            history_cards(self.driver)[-1]
        )

    def order_num(self):
        return len(history_cards(self.driver))

    def decline_last_order(self):
        old_num = self.order_num()
        last_card = history_cards(self.driver)[-1]
        last_card.click()
        decline_button(last_card).click()
        self.wait_decline_button_is_visible(last_card)
        decline_button(last_card).click()
        self.wait_order_declined(old_num)

    def wait_order_declined(self, old_order_num):
        return WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: self.order_num() < old_order_num
        )

    def wait_decline_button_is_visible(self, card):
        return WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: decline_button(card).is_displayed()
        )


def decline_button(card):
    return card.find_element_by_css_selector(
        'button[class^="neon-button"]'
    )


def product_name(card):
    return card.find_element_by_css_selector(
        'div.order-card__product-section-list_name'
    ).get_attribute('innerText')


def product_price(card):
    return card.find_element_by_css_selector(
        'div.order-card__product-section-list_price'
    ).get_attribute('innerText')


def title(driver):
    return driver.find_element_by_css_selector(
        'h1.order-history__main-content_title'
    )


def history_cards(driver):
    return driver.find_elements_by_css_selector(
        '.order-card__container'
    )


def restaurant_name(card):
    return card.find_element_by_css_selector(
        '.order-card__title-section_title'
    ).get_attribute('innerText')
