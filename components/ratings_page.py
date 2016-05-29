# -*- coding: utf-8 -*-

from components.component import Component


class RatingsBlock(Component):
    IMPORT_RATING = '//span[@class="button__text" and contains(text(),"Загрузить оценки")]'
    CHOOSE_FILM = '//div[@class="button__text" and contains(text(),"Выбрать фильмы")]'
    CHOOSE_SERIES = '//div[@class="button__text" and contains(text(),"Выбрать сериалы")]'
    CHOOSE_TVSHOW = '//div[@class="button__text" and contains(text(),"Выбрать телешоу")]'

    BASE_URL = 'https://afisha.mail.ru'
    IMPORT_RATING_URL = BASE_URL + '/user/ratings/import/'
    CHOOSE_FILM_URL = BASE_URL + '/cinema/online/'
    CHOOSE_SERIES_URL = BASE_URL + '/series/online/'
    CHOOSE_TVSHOW_URL = BASE_URL + '/tvshow/online/'

    def click_import_rating(self):
        self.click(self.IMPORT_RATING)

    def click_choose_film(self):
        self.click(self.CHOOSE_FILM)

    def click_choose_series(self):
        self.click(self.CHOOSE_SERIES)

    def click_choose_tvshow(self):
        self.click(self.CHOOSE_TVSHOW)
