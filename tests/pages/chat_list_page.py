from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class ChatListPage(Page):
    PATH = 'support/chats'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: chat_item(d).is_displayed()
        )

    def click_first_chat_card(self):
        chat_items(self.driver)[-1].click()

    def click_user_chat_card(self, user_id):
        chat_card(self.driver, user_id).click()


def chat_item(driver):
    return driver.find_element_by_css_selector('div[class^="chat-item"]')


def chat_items(driver):
    return driver.find_elements_by_css_selector('div[class^="chat-item"]')


def chat_card(driver, user_id):
    return driver.find_element_by_css_selector('.chat-item.chat-item-%d' % user_id)
