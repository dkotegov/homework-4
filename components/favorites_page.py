# -*- coding: utf-8 -*-

from components.component import *


class FavoritesBlock(Component):
    BASE_URL = 'https://afisha.mail.ru/'
    FILMS_BUTTON_URL = BASE_URL + 'user/favorites/cinema/'
    SERIES_BUTTON_URL = BASE_URL + 'user/favorites/series/'
    CHOOSE_FILMS_BUTTON_URL = 'cinema/online/'
    CHOOSE_SERIES_BUTTON_URL = 'series/online/'

    TEST_FILM_URL = BASE_URL + 'cinema/movies/709388_1_1/'
    ADD_FILM_BUTTON = '//div[contains(text(),"Хочу посмотреть")]'

    EMPTY_TITLE = '//span[contains(text(),"ПОКА ВАШ СПИСОК ПУСТ")]'

    FILMS_BUTTON = '//span[@class="blockmenu__item__link" and contains(text(),"Фильмы")]'
    SERIES_BUTTON = '//span[@class="blockmenu__item__link" and contains(text(),"Сериалы")]'
    CHOOSE_FILMS_BUTTON = '//div[contains(text(),"Выбрать фильмы")]'
    CHOOSE_SERIES_BUTTON = '//div[contains(text(),"Выбрать сериалы")]'

    SORT_DATE = '//u[contains(text(),"Дате добавления")]'
    SORT_VOICE = '//u[contains(text(),"Количеству голосов")]'
    SORT_RATE = '//u[contains(text(),"Рейтингу")]'
    SORT_NAME = '//u[contains(text(),"Названию")]'

    SORT_DATE_URL = BASE_URL + 'user/favorites/cinema/?order=created#list'
    SORT_VOICE_URL = BASE_URL + 'user/favorites/cinema/?order=rate_count#list'
    SORT_RATE_URL = BASE_URL + 'user/favorites/cinema/?order=rate_val#list'
    SORT_NAME_URL = BASE_URL + 'user/favorites/cinema/?order=name#list'

    FILM_TITLE = '//a[contains(text(),"1+1")]'
    FILM_IMG = '//div[@class="pm-itemevent__pic"]'
    FILM_CITY = '//a[contains(text(),"Франция")]'
    FILM_YEAR = '//a[contains(text(),"2011")]'
    DRAMA_BUTTON = '//a[contains(text(),"драма")]'
    COMEDY_BUTTON = '//a[contains(text(),"комедия")]'
    BIO_BUTTON = '//a[contains(text(),"биография")]'
    WATCH_BUTTON = '//div[contains(text(),"Смотреть бесплатно")]'
    REMOVE_BUTTON = '//span[contains(text(),"Убрать из списка")]'

    FILM_CITY_URL = BASE_URL + 'cinema/all/fra/'
    FILM_YEAR_URL = BASE_URL + 'cinema/all/2011/'
    DRAMA_BUTTON_URL = BASE_URL + 'cinema/all/drama/'
    COMEDY_BUTTON_URL = BASE_URL + 'cinema/all/komedija/'
    BIO_BUTTON_URL = BASE_URL + 'cinema/all/biografija/'
    WATCH_BUTTON_URL = BASE_URL + 'cinema/movies/709388_1_1/?autoplay=1#watch'

    def click_films_button(self):
        self.click(self.FILMS_BUTTON)

    def click_series_button(self):
        self.click(self.SERIES_BUTTON)

    def click_choose_films_button(self):
        self.click(self.CHOOSE_FILMS_BUTTON)

    def click_choose_series_button(self):
        self.click(self.CHOOSE_SERIES_BUTTON)

    def add_or_remove_film(self):  # same button can add or delete film
        self.driver.get(self.TEST_FILM_URL)
        self.click(self.ADD_FILM_BUTTON)

    def click_film_title(self):
        self.click(self.FILM_TITLE)

    def click_film_img(self):
        self.click(self.FILM_IMG)

    def click_film_city(self):
        self.click(self.FILM_CITY)

    def click_film_year(self):
        self.click(self.FILM_YEAR)

    def click_film_drama(self):
        self.click(self.DRAMA_BUTTON)

    def click_film_comedy(self):
        self.click(self.COMEDY_BUTTON)

    def click_film_bio(self):
        self.click(self.BIO_BUTTON)

    def click_film_watch(self):
        self.click(self.WATCH_BUTTON)

    def click_film_remove(self):
        self.click(self.REMOVE_BUTTON)



