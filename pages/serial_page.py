from components.popup_film import PopupFilm
from components.infoblock_film import InfoblockFilm
from pages.base import BasePage
from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from components.card import Card
from components.player import Player


class SerialPage(BasePage):
    """
    Страница сериала
    """

    def __init__(self, driver):
        self.PATH = 'serials'
        self.popup_film = PopupFilm(driver)
        super(SerialPage, self).__init__(driver, self.popup_film.locators.root)
        self.infoblock_film = InfoblockFilm(self.driver)
        self.navbar_form = NavbarForm(self.driver)
        self.card = Card(self.driver)
        self.player = Player(self.driver)
        self.auth_form = AuthForm(driver)

    def open_popup(self):
        self.popup_film.open_popup()

    def click_season_button(self) -> bool:
        return self.popup_film.click_season_if_exist()

    def check_season_changed(self) -> bool:
        return self.popup_film.check_season_changed()

    def click_serial_episode(self) -> bool:
        return self.popup_film.click_episode()

    def check_player_is_open(self) -> bool:
        return self.popup_film.check_player_is_open()

    def open_infoblock(self):
        self.infoblock_film.open_infoblock()

    def click_infoblock_details(self):
        self.infoblock_film.click_infoblock_tab_button("Детали")

    def check_infoblock_details_open(self) -> bool:
        return self.infoblock_film.check_details_clicked()

    def click_infoblock_seasons(self):
        self.infoblock_film.click_infoblock_tab_button("Сезоны")

    def check_infoblock_seasons_open(self) -> bool:
        return self.infoblock_film.check_seasons_clicked()

    def click_infoblock_season_button(self):
        self.infoblock_film.click_season_button()

    def check_episodes_open(self) -> bool:
        return self.infoblock_film.check_episodes_open()

    def click_episode(self):
        self.infoblock_film.click_episode()

    def check_player_open(self) -> bool:
        return self.infoblock_film.check_player_open()

    def close_infoblock(self):
        self.infoblock_film.click_close_button()

    def check_infoblock_close(self) -> bool:
        return self.infoblock_film.check_infoblock_closed()

    def open_auth_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_login_button()

    def auth(self, email, password):
        self.auth_form.set_email(email)
        self.auth_form.set_password(password)
        self.auth_form.submit()

    def open_card_player(self):
        self.card.click_player_btn()

    def move_to_card(self):
        self.card.move_to()

    def check_auth(self) -> bool:
        return self.navbar_form.check_auth_is_right()

    def check_player_appearance(self) -> bool:
        return self.player.check_appearance()

    def check_switch_next_episode(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_next_ep_btn()
        return self.player.check_next_ep()

    def check_switch_prev_episode(self) -> bool:
        self.player.move_to_player_bar()
        self.player.click_on_next_ep_btn()
        self.player.click_on_prev_ep_btn()
        return self.player.check_prev_ep()
