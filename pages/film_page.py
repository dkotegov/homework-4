import time

from components.filter import Filter
from components.infoblock_film import InfoblockFilm
from pages.base import BasePage


class FilmPage(BasePage):
    """
    Страница фильма
    """
    def __init__(self, driver):
        self.PATH = 'movies'
        self.infoblock_film = InfoblockFilm(driver)
        super(FilmPage, self).__init__(driver, self.infoblock_film.locators.root)
        self.filter = Filter(self.driver)

    def open_infoblock(self):
        self.infoblock_film.open_infoblock()

    def click_add_mylist_button(self) -> bool:
        return self.infoblock_film.click_my_list_button()

    def close_infoblock(self):
        self.infoblock_film.click_close_button()

    def check_infoblock_close(self) -> bool:
        return self.infoblock_film.check_infoblock_closed()

    def find_subscription_film(self):
        self.filter.click_genres_button()
        genres = self.filter.get_genres_refs()
        for k in range(0, len(genres)):
            genres = self.filter.get_genres_refs()
            self.filter.click_genre(genres[k])
            films = self.infoblock_film.get_films()
            films_len = len(films)

            for i in range(0, films_len):
                films = self.infoblock_film.get_films()
                self.infoblock_film.click_film(films[i])
                if self.infoblock_film.check_subscription_label():
                    return
                self.infoblock_film.click_close_button()
                self.infoblock_film.check_infoblock_closed()

            self.open()
            self.filter.click_genres_button()

    def click_play_button(self):
        self.infoblock_film.click_play_button()

    def check_subscription_popup_open(self) -> bool:
        return self.infoblock_film.check_subscription_popup_open()
