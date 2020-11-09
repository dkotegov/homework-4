from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.page import Page


class ManageOrderPage(Page):
    def __init__(self, driver, rest_id):
        super().__init__(driver)
        self.rest_id = rest_id
        self.PATH = 'admin/restaurants/%d/orders' % rest_id

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: header(d).is_displayed() and
                      len(status_cards(d)) > 0
        )

    def last_order_status(self):
        return status_name(
            status_cards(self.driver)[-1]
        )

    def status_cards_num(self):
        return len(status_cards(self.driver))

    def last_order_set_next_status(self):
        last_card = status_cards(self.driver)[-1]
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: EC.element_to_be_clickable(last_card)
        )
        status(last_card).click()

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: next_status_button(last_card).is_displayed()
        )

        next_status_button(last_card).click()
        self.wait_visible()

    def delete_last_notif(self):
        self.show_notifs()

        notifs = notifications(self.driver)
        if len(notifs) > 0:
            notif_del_button(
                notifs[-1]
            ).click()

        self.hide_notifs()

    def wait_notif_appear(self):
        return WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: notif_container(d).is_displayed()
        )

    def show_notifs(self):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: notif_icon(d).is_displayed()
        )
        notif_icon(self.driver).click()
        self.wait_notif_appear()

    def hide_notifs(self):
        ActionChains(self.driver).move_by_offset(100, 100).click().perform()
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: not notif_hider(d).is_displayed()
        )

    def last_notif_message(self):
        self.show_notifs()
        message = notif_message(
            notifications(self.driver)[-1]
        )
        self.hide_notifs()
        return message


def clear_notif_text(text):
    first = text.index('"') + 1
    last = text.index('"', first)
    return text[first : last]


def notif_message(notif):
    return clear_notif_text(
        notif.get_attribute('innerText')
    )


def notif_hider(driver):
    return driver.find_element_by_css_selector(
        '.notif-popup__hider'
    )


def notif_del_button(notif):
    return notif.find_element_by_css_selector(
        '.neon-button '
    )


def notifications(driver):
    return driver.find_elements_by_css_selector(
        '.notification'
    )


def notif_container(driver):
    return driver.find_element_by_css_selector(
        '.notif-container'
    )


def notif_icon(driver):
    return driver.find_element_by_css_selector(
        '#notif-icon',
    )


def header(driver):
    return driver.find_element_by_css_selector(
        'nav[class="icon-bar iconed-header__icon-bar"]'
    )


def status_cards(driver):
    return driver.find_elements_by_css_selector(
        '.restaurant-item '
    )


def status(card):
    return card.find_element_by_css_selector(
        '.order-item__name'
    )


def status_name(card):
    return status(card).get_attribute('innerText')


def next_status_button(card):
    return card.find_element_by_css_selector(
        'button[class^="neon-button"]'
    )
