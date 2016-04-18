# -*- coding: utf-8 -*-

from components.component import *


class ProfileBlock(Component):
    ABOUT_BTN = '//span[contains(text(),"О персоне") and @class="link__text"]'
    BIO_BTN = '//span[contains(text(),"Биография") and @class="link__text"]'
    FILMS_BTN = '//span[contains(text(),"Фильмы") and @class="link__text"]'
    NEWS_BTN = '//span[contains(text(),"Новости") and @class="link__text"]'

    BASE_URL = 'https://afisha.mail.ru/person/471877_sasha_grey/'
    ABOUT_URL = BASE_URL + '#about'
    BIO_URL = BASE_URL + '#descr'
    FILMS_URL = BASE_URL + '#best_event'
    NEWS_URL = BASE_URL + '#news'

    FISHES_BTN = '//a[contains(text(),"Рыбы")]'
    FISHES_URL = 'https://horo.mail.ru/prediction/pisces/today/'

    WIKI_BTN = '//a[contains(text(),"Саша Грэй в Википедии")]'
    WIKI_URL = 'https://ru.wikipedia.org/wiki/index.html?curid=1675032'

    FILM_TITLE = '//a[contains(text(),"Девушка по вызову")]'
    FILM_YEAR = '//a[contains(text(),"2009")]'
    FILM_COUNTRY = '//a[contains(text(),"США")]'
    FILM_REZH = '//a[contains(text(),"Стивен Содерберг")]'
    FILM_ROLE = '//a[contains(text(),"Крис Сантос")]'

    AFISHA_URL = 'https://afisha.mail.ru/'
    FILM_TITLE_URL = AFISHA_URL + 'cinema/movies/507814_devushka_po_vyzovu/'
    FILM_YEAR_URL = AFISHA_URL + 'cinema/all/2009/'
    FILM_COUNTRY_URL = AFISHA_URL + 'cinema/all/usa/'
    FILM_REZH_URL = AFISHA_URL + 'person/447638_steven_soderbergh/'
    FILM_ROLE_URL = AFISHA_URL +'person/502619_chris_santos/'

    # ALL_FILMS_BTN = '//span[@class="link__text" and contains(text(),"Саша Грэй: все фильмы и сериалы")]'
    ALL_FILMS_BTN = '//a[@href="/person/471877_sasha_grey/movies/" and @class="link link_underline link_icon"]'
    ALL_FILMS_URL = AFISHA_URL + 'person/471877_sasha_grey/movies/'

    ARTICLE_BTN = '//a[contains(text(),"Саша Грэй показала «Открытые окна» в Москве")]'
    ARTICLE_URL = AFISHA_URL + 'cinema/articles/44183/'

    BORN_TODAY_BTN = '//span[contains(text(),"Сегодня родились") and @class="hdr__inner"]'
    BORN_TODAY_URL = AFISHA_URL + 'person/birthday/'

    # STAR_NEWS = '//span[contains(text(),"Новости о звездах")]'
    STAR_NEWS = '//a[@href="/msk/stars/articles/" and @class="hdr__text"]'
    ALL_STAR_NEWS = '//span[contains(text(),"Все новости о звездах")]'
    STAR_NEWS_URL = AFISHA_URL + 'msk/stars/articles/'

    def click_about(self):
        self.click(self.ABOUT_BTN)

    def click_bio(self):
        self.click(self.BIO_BTN)

    def click_films(self):
        self.click(self.FILMS_BTN)

    def click_news(self):
        self.click(self.NEWS_BTN)

    def click_fishes(self):
        self.click(self.FISHES_BTN)

    def click_wiki(self):
        self.click(self.WIKI_BTN)

    def click_title(self):
        self.click(self.FILM_TITLE)

    def click_year(self):
        self.click(self.FILM_YEAR)

    def click_country(self):
        self.click(self.FILM_COUNTRY)

    def click_rezh(self):
        self.click(self.FILM_REZH)

    def click_role(self):
        self.click(self.FILM_ROLE)

    def click_all_films(self):
        self.click(self.ALL_FILMS_BTN)

    def click_article(self):
        self.click(self.ARTICLE_BTN)

    def click_born_today(self):
        self.click(self.BORN_TODAY_BTN)

    def click_star_news(self):
        self.click(self.STAR_NEWS)

    def click_all_star_news(self):
        self.click(self.ALL_STAR_NEWS)
