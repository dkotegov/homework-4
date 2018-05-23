from selenium.common.exceptions import TimeoutException

from components.games_list import GamesList
from components.main_up_toolbar import MainUpToolbar
from components.page import Page


class GamesVitrine(Page):
    PAGE = '/vitrine'

    def __init__(self, driver):
        super(GamesVitrine, self).__init__(driver)
        self.games_list = GamesList(self.driver)
        self.main_up_toolbar = MainUpToolbar(self.driver)

    def invite_friend_to_the_game(self):
        el_game = self.games_list.get_game()
        self.get_hover(el_game)

        self.games_list.get_invite_friends_button().click()

        if self.games_list.get_lock():
            return False

        el_user = self.games_list.get_user_avatar()
        self.get_hover(el_user)
        self.games_list.get_choose_user().click()
        self.games_list.get_confirm_user().click()
        return True

    def check_invite_button(self):
        self.games_list.get_invite()
        self.games_list.get_invite_friends_button().click()
        self.games_list.get_back_button().click()

    def participate_to_game(self):
        self.get_hover(self.games_list.get_hover_right_arrow())
        self.games_list.get_right_arrow().click()
        self.games_list.get_blood_button_game().click()




