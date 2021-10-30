
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page


class UserChats(Page):
    PATH = "user/chats"

    TITLE = ".chat-message-head-info-user__name"
    MY_PRODUCTS = "#profile-menu-posts"

    def change_path(self, path):
        self.PATH = "user/chat/" + path

    def get_title(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.helpers.get_element(self.TITLE).text

    def click_my_products(self):
        self.helpers.click_button(self.MY_PRODUCTS)
