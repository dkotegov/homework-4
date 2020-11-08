from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class OrderPage(Page):
    PATH = 'checkout'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: checkout_button(d).is_displayed() and
                      email_input(d).is_displayed() and
                      phone_input(d).is_displayed()
        )

    def set_phone(self, text):
        phone = phone_input(self.driver)
        phone.clear()
        phone.send_keys(text)

    def phone(self):
        return phone_input(self.driver).get_attribute('value')

    def phone_error(self):
        return phone_error(self.driver).get_attribute('innerText')

    def set_email(self, text):
        email = email_input(self.driver)
        email.clear()
        email.send_keys(text)

    def email_error(self):
        return email_error(self.driver).get_attribute('innerText')

    def click_checkout_button(self):
        checkout_button(self.driver).click()

    def wait_email_error(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: len(email_error(d).get_attribute('innerText')) > 0
        )

    def wait_phone_error(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: len(phone_error(d).get_attribute('innerText')) > 0
        )

def phone_error(driver):
    return driver.find_element_by_css_selector(
        'div#order-checkout__phone-input-wrapper_err'
    )


def email_error(driver):
    return driver.find_element_by_css_selector(
        'div#order-checkout__email-input-wrapper_err'
    )


def email_input(driver):
    return driver.find_element_by_css_selector(
        'input#order-checkout__email-input'
    )


def phone_input(driver):
    return driver.find_element_by_css_selector(
        'input#order-checkout__phone-input'
    )


def checkout_button(driver):
    return driver.find_element_by_css_selector(
        'button[class="product-card-button button"]'
    )
