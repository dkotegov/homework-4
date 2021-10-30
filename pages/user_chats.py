
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default_page import DefaultPage


class UserChats(DefaultPage):
    PATH = "user/chats"

    TITLE = ".chat-message-head-info-user__name"
    MY_PRODUCTS = "#profile-menu-posts"

    def change_path(self, path):
        self.PATH = "user/chat/" + path

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text

    def click_my_products(self):
        self.__click_button__(self.MY_PRODUCTS)
