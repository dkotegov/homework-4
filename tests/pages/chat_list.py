from tests.pages.base import Page


class ChatListPage(Page):
    """
    Стриница с чатами чата
    """

    RESTAURANT_NAME = '//h2[@class="chat-container__header__name"]'
    CHAT_RESTAURANT_NAME = '//h3[@class="chat-node__name"]'
    CHAT_RESTAURANT_NAME_BUTTON = '//h3[contains(text(),"{}") and @class="chat-node__name"]'

    def __init__(self, driver):
        self.PATH = 'profile/chats'
        super(ChatListPage, self).__init__(driver)

    def get_restaurant_name(self):
        return self.driver.find_element_by_xpath(self.RESTAURANT_NAME).text

    def get_all_chats(self):
        elements = self.driver.find_elements_by_xpath(self.CHAT_RESTAURANT_NAME)
        chats = []
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.CHAT_RESTAURANT_NAME)
            chats.append(elements[i].text)
        return chats

    def click_chat(self, name_chat):
        return self.driver.find_element_by_xpath(self.CHAT_RESTAURANT_NAME_BUTTON.format(name_chat)).click()

