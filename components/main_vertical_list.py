
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class MainVerticalList(BaseComponent):
    FRIENDS_BUTTON = "//i[contains(@class,'ic_nav_friends-v2')]"
    GAMES_BUTTON = "//i[contains(@class, 'ic_nav_games-v2')]"

    def get_friends(self):
        return self.get_clickable_element(self.FRIENDS_BUTTON)

    def get_games(self):
        return self.get_clickable_element(self.GAMES_BUTTON)

