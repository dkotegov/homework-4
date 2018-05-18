from components.current_game import CurrentGame
from components.page import Page


class GamePage(Page):

    def block_notifications(self):
        current_game = CurrentGame(self.driver)
        current_game.get_information_about_the_game_button()
        current_game.get_notification_button()
        current_game.get_confirm_button()
