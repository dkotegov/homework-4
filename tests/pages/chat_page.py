from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class ChatPage(Page):
    PATH = 'support'
    DEFAULT_MESSAGE = __name__

    def wait_visible(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: message_input(d).is_displayed() and
                      send_button(d).is_displayed()
        )

    def wait_message_text_visible(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: message_text(d).is_displayed()
        )

    def send_message(self, message):
        message_input(self.driver).send_keys(message)
        send_button(self.driver).click()
        self.wait_message_sent()

    def send_start_message(self):
        self.send_message(self.DEFAULT_MESSAGE)

    def wait_message_sent(self, ):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: send_button(d).get_attribute('disabled') is None
        )

    def message_number(self):
        return len(messages(self.driver))

    @property
    def last_message(self):
        return messages(self.driver)[-1].get_attribute('innerText')


def message_input(driver):
    return driver.find_element_by_css_selector('input[class="message_input input"]')


def message_text(driver):
    return driver.find_element_by_css_selector('p.messgae__text')


def send_button(driver):
    return driver.find_element_by_css_selector('button[class="neon-button send_button"]')


def messages(driver):
    return driver.find_elements_by_css_selector('p.messgae__text')
