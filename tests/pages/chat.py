from tests.pages.base import Page
from selenium.webdriver.common.keys import Keys


class ChatPage(Page):
    """
    Стриница чата
    """

    RESTAURANT_NAME = '//h2[@class="chat-container__header__name"]'
    MESSAGE = '//p[@data-messageid]'
    BUTTON_SUBMIT = '//button[@id="js__send-button"]'
    INPUT_MESSAGE = '//input[@class="chat-send__input"]'

    def __init__(self, driver, chat_id):
        self.chat_id = chat_id
        self.PATH = 'profile/chats/' + str(chat_id)
        super(ChatPage, self).__init__(driver)

    def get_restaurant_name(self):
        return self.driver.find_element_by_xpath(self.RESTAURANT_NAME).text

    def get_all_messages(self):
        elements = self.driver.find_elements_by_xpath(self.MESSAGE)
        messages = []
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.MESSAGE)
            messages.append(elements[i].text)
        return messages

    def set_new_message(self, message):
        elem = self.driver.find_element_by_xpath(self.INPUT_MESSAGE)
        elem.clear()
        elem.send_keys(message)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.BUTTON_SUBMIT).click()

    def click_enter(self):
        self.driver.find_element_by_xpath(self.INPUT_MESSAGE).send_keys(Keys.ENTER)

    def refresh_page(self):
        self.driver.refresh()
