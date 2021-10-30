from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from helpers import Page
from components import SettingsCard


class UserChats(Page):
    PATH = "user/chats"

    TITLE = ".chat-message-head-info-user__name"

    @property
    def settings_card(self):
        return SettingsCard(self.driver)

    def change_path(self, path):
        self.PATH = "user/chat/" + path

    def page_exist(self):
        self.helpers.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.helpers.get_element(self.TITLE) is not None
