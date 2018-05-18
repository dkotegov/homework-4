from components.games_list import GamesList
from components.main_up_toolbar import MainUpToolbar
from components.page import Page


class GamesVitrine(Page):

    def __init__(self, driver):
        super(GamesVitrine, self).__init__(driver)
        self.games_list = GamesList(self.driver)
        self.main_up_toolbar = MainUpToolbar(self.driver)

    def invite_friend_to_the_game(self):
        el_game = self.games_list.get_game()
        self.get_hover(el_game)
        self.main_up_toolbar.get_split_for_app_id()
        self.games_list.get_invite_friends_button().click()

        el_user = self.games_list.get_user_avatar()
        self.get_hover(el_user)
        self.games_list.get_choose_user().click()
        self.games_list.get_confirm_user().click()
