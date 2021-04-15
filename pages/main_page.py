from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from components.reg_form import RegForm
from components.popup_film import PopupFilm
from components.infoblock_film import InfoblockFilm
from components.preview import Preview
from components.player import Player
from components.card import Card
from pages.base import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        self.PATH = 'browse'
        self.auth_form = AuthForm(driver)
        super(MainPage, self).__init__(driver, self.auth_form.locators.root)
        self.reg_form = RegForm(driver)
        self.navbar_form = NavbarForm(self.driver)
        self.popup_film = PopupFilm(self.driver)
        self.infoblock_film = InfoblockFilm(self.driver)
        self.preview = Preview(self.driver)
        self.player = Player(self.driver)
        self.card = Card(self.driver)

    def open_auth_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_login_button()

    def open_exit_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_exit_button()

    def open_reg_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_reg_button()
    
    def move_to_reg_popup(self):
        self.auth_form.click_reg_btn()

    def auth(self, email, password):
        self.auth_form.set_email(email)
        self.auth_form.set_password(password)
        self.auth_form.submit()
    
    def open_preview_info_popup(self):
        self.preview.click_info_button()
    
    def open_card_info_block_via_card_click(self):
        self.card.click()
    
    def open_card_info_block(self):
        self.card.click_info_block_btn()
    
    def open_card_player(self):
        self.card.click_player_btn()
    
    def move_to_card(self):
        self.card.move_to()
    
    def open_player(self):
        self.preview.click_play_button()
    
    def open_search_line(self):
        self.navbar_form.click_search_magnifier_to_open()
    
    def search_by_click(self):
        self.navbar_form.click_search_magnifier_to_search()
    
    def search_by_Enter(self):
        self.navbar_form.press_Enter_to_search()
    
    def input_text_into_search_line(self, text: str = 'a'):
        self.open_search_line()
        self.navbar_form.set_search_line_text(text)
    
    def choise_prompt(self):
        self.navbar_form.choise_prompt_label()

    def check_auth(self) -> bool:
        return self.navbar_form.check_auth_is_right()

    def check_exit(self) -> bool:
        return self.navbar_form.check_exit_is_right()

    def check_reg_popup_appearance(self) -> bool:
        return self.reg_form.check_appearance()

    def open_popup(self):
        self.popup_film.open_popup()

    def click_infoblock_like_button(self):
        self.popup_film.click_like_button()

    def check_infoblock_liked(self) -> bool:
        return self.popup_film.check_like_clicked()

    def click_infoblock_dislike_button(self):
        self.popup_film.click_dislike_button()

    def check_infoblock_disliked(self) -> bool:
        return self.popup_film.check_dislike_clicked()

    def click_genre(self):
        self.popup_film.click_genre_anchor()

    def check_genre_redirect(self) -> bool:
        return self.popup_film.check_genre_redirect()

    def click_actor(self):
        self.popup_film.click_actor_anchor()

    def check_actor_redirect(self) -> bool:
        return self.popup_film.check_actor_redirect()

    def click_director(self):
        self.popup_film.click_director_anchor()

    def check_director_redirect(self) -> bool:
        return self.popup_film.check_director_redirect()

    def is_same_films(self) -> bool:
        return self.popup_film.is_same_films()

    def click_same_film(self):
        self.popup_film.click_same_film()

    def check_same_film_popup_open(self) -> bool:
        return self.popup_film.check_same_film_name()
    
    def check_auth_password_error(self, error_text: str) -> bool:
        return self.auth_form.check_password_error(error_text)
    
    def check_auth_email_error(self, error_text: str) -> bool:
        return self.auth_form.check_email_error(error_text)
    
    def check_info_popup_appearance(self) -> bool:
        return self.popup_film.check_appearance()
    
    def check_info_block_appearance(self) -> bool:
        return self.infoblock_film.check_appearance()
    
    def check_player_appearance(self) -> bool:
        return self.player.check_appearance()
    
    def check_search_line_appearance(self) -> bool:
        return self.navbar_form.check_search_line_appearance()
    
    def check_search_line_disappearance(self) -> bool:
        return self.navbar_form.check_search_line_disappearance()
    
    def check_search_prompt_window_appearance(self) -> bool:
        return self.navbar_form.check_search_prompt_window_appearance()

    def click_like(self):
        self.infoblock_film.click_like_button()

    def click_dislike(self):
        self.infoblock_film.click_dislike_button()

    def click_add_my_list_infoblock(self):
        self.infoblock_film.click_add_my_list_button()

    def check_auth_popup_open(self) -> bool:
        return self.infoblock_film.check_auth_popup_open()

    def open_infoblock(self):
        self.infoblock_film.open_infoblock()

    def click_add_my_list_popup(self):
        self.popup_film.click_add_my_list_button()

    def check_add_my_list_clicked(self) -> bool:
        return self.popup_film.check_add_my_list_clicked()

    def regist(self, email, password, repeated_password):
        self.reg_form.set_email(email)
        self.reg_form.set_password(password)
        self.reg_form.set_repeated_password(repeated_password)
        self.reg_form.submit()

    def check_registr(self) -> bool:
        return self.navbar_form.check_auth_is_right()

    def check_regist_email_error(self, error_text: str) -> bool:
        return self.reg_form.check_email_error(error_text)

    def check_regist_password_error(self, error_text: str) -> bool:
        return self.reg_form.check_password_error(error_text)

    def check_repeated_regist_password_error(self, error_text: str) -> bool:
        return self.reg_form.check_repeated_password_error(error_text)

    def check_auth_popup_appear(self) -> bool:
        self.reg_form.click_auth_btn()
        return self.auth_form.check_appearance()

    def check_closed_popup(self) -> bool:
        self.reg_form.click_close_btn()
        return self.reg_form.check_disappear()

