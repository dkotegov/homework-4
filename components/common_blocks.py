# -*- coding: utf-8 -*-

from components.component import *


# TODO: changing button 'Забытые актрисы', '100 фильмов для киноманов'
# TODO: search field
# TODO: test hover?
# TODO: ad block test


class MainHeader(Component):
    BASE_URL = 'https://afisha.mail.ru/'
    RECOMMENDED_URL = BASE_URL + 'user/recommended/'
    RATINGS_URL = BASE_URL + 'user/ratings/cinema/'
    FAVORITES_URL = BASE_URL + 'user/favorites/'

    TEST_USER_LOGIN = 'valeriy-test'
    TEST_USER_DOMAIN = '@mail.ru'
    TEST_USER_PASSWORD = 'passw0rd'

    LOGIN_BUTTON = '//a[contains(text(),"Вход")]'
    LOGIN_INPUT = '//input[@id="ph_login"]'
    # DOMAIN_INPUT = '//select[@name="Domain"]/option[@value="@bk.ru"]'
    # DOMAIN_INPUT = '//select[@name="Domain"]'
    PASSWORD_INPUT = '//input[@id="ph_password"]'
    LOGIN_SUBMIT_BUTTON = '//span[@class="js-control js-control-login x-ph__button x-ph__button_action"]'
    # LOGIN_SUBMIT_BUTTON = '//span[contains(text(),"Войти")]'

    LOGO_BUTTON = '//img[@class="pm-logo__link__pic"]'
    RECOMMENDED_BUTTON = '//span[contains(text(),"Рекомендации")]'
    RATINGS_BUTTON = '//span[@name="clb18426049"]'
    FAVORITES_BUTTON = '//span[@name="clb16611312"]'

    def click_logo(self):
        self.click(self.LOGO_BUTTON)

    def click_recommended(self):
        self.click(self.RECOMMENDED_BUTTON)

    def click_ratings(self):
        self.click(self.RATINGS_BUTTON)

    def click_favorites(self):
        self.click(self.FAVORITES_BUTTON)

    def login(self):
        if self.driver.find_element_by_xpath(self.LOGIN_BUTTON):
            self.click(self.LOGIN_BUTTON)
            self.send_keys(self.LOGIN_INPUT, self.TEST_USER_LOGIN)
            self.send_keys(self.PASSWORD_INPUT, self.TEST_USER_PASSWORD)
            self.click(self.LOGIN_SUBMIT_BUTTON)
            # self.click(self.LOGO_BUTTON)


class NavBar(Component):
    CINEMA_BUTTON = '//span[contains(text(),"Фильмы")]'
    SERIES_BUTTON = '//span[contains(text(),"Сериалы")]'
    TVSHOW_BUTTON = '//span[contains(text(),"Телешоу")]'
    TV_BUTTON = '//span[contains(text(),"Телепрограмма")]'
    STARS_BUTTON = '//span[contains(text(),"Звёзды")]'

    BASE_URL = 'https://afisha.mail.ru/'
    TV_BASE_URL = 'https://tv.mail.ru/'
    CINEMA_URL = BASE_URL + 'msk/cinema/'
    SERIES_URL = BASE_URL + 'msk/series/'
    TVSHOW_URL = BASE_URL + 'msk/tvshow/'
    TV_URL = BASE_URL + 'moskva/'
    STARS_URL = BASE_URL + 'stars/'

    CINEMA_DROPDOWN = {'KINOAFISHA': '//span[contains(text(),"Киноафиша")]',
                       'ONLINE': '//span[contains(text(),"Фильмы онлайн")]',
                       'TOP': '//span[contains(text(),"Лучшие фильмы")]',
                       'SOON': '//span[contains(text(),"Календарь кинопремьер")]',
                       'SELECTIONS': '//span[contains(text(),"Подборки")]',
                       'AWARDS': '//span[contains(text(),"Премии")]',
                       'PLACES': '//span[contains(text(),"Кинотеатры")]',
                       'ARTICLES': '//span[contains(text(),"Новости")]',
                       }

    CINEMA_DROPDOWN_URLS = {'KINOAFISHA': BASE_URL + 'msk/cinema/kinoafisha/',
                            'ONLINE': BASE_URL + 'cinema/online/',
                            'TOP': BASE_URL + 'cinema/top/',
                            'SOON': BASE_URL + 'cinema/soon/#soon',
                            'SELECTIONS': BASE_URL + 'cinema/selections/',
                            'AWARDS': BASE_URL + 'awards/',
                            'PLACES': BASE_URL + 'msk/cinema/places/',
                            'ARTICLES': BASE_URL + 'msk/cinema/articles/',
                            }

    SERIES_DROPDOWN = {'TOP': '//span[contains(text(),"Лучшие сериалы")]',
                       'ONLINE': '//span[contains(text(),"Сериалы онлайн")]',
                       'SELECTIONS': '//span[contains(text(),"Подборки")]',
                       'ALL': '//span[contains(text(),"Все сериалы")]',
                       'ARTICLES': '//span[contains(text(),"Подборки")]',
                       }

    SERIES_DROPDOWN_URLS = {'TOP': BASE_URL + 'series/top/',
                            'ONLINE': BASE_URL + 'series/online/',
                            'SELECTIONS': BASE_URL + 'series/selections/',
                            'ALL': BASE_URL + 'series/all/',
                            'ARTICLES': BASE_URL + 'msk/series/articles/',
                            }

    TVSHOW_DROPDOWN = {'TOP': '//span[contains(text(),"Лучшие телешоу")]',
                       'ONLINE': '//span[contains(text(),"Телешоу онлайн")]',
                       'ALL': '//span[contains(text(),"Все телешоу")]',
                       'ARTICLES': '//span[contains(text(),"Новости")]',
                       }

    TVSHOW_DROPDOWN_URLS= {'TOP': BASE_URL + 'tvshow/top/',
                           'ONLINE': BASE_URL + 'tvshow/online/',
                           'ALL': BASE_URL + 'tvshow/all/',
                           'ARTICLES': BASE_URL + 'msk/tvshow/articles/',
                           }

    TV_DROPDOWN = {'CENTRAL': '//span[contains(text(),"Центральные")]',
                           'LOCAL': '//span[contains(text(),"Местные")]',
                           'SPORT': '//span[contains(text(),"Спортивные")]',
                           'MOVIES_SERIES': '//span[contains(text(),"Фильмы и Сериалы")]',
                           'NEWS': '//span[contains(text(),"Новостные")]',
                          }

    TV_DROPDOWN_URLS = {'CENTRAL': TV_BASE_URL + 'moskva/central/',
                                'LOCAL': TV_BASE_URL + 'moskva/local/',
                                'SPORT': TV_BASE_URL + 'moskva/sport/',
                                'MOVIES_SERIES': TV_BASE_URL + 'moskva/movies_series/',
                                'NEWS': TV_BASE_URL + 'moskva/news/',
                               }

    STARS_DROPDOWN = {'ARTICLES': '//span[contains(text(),"Новости")]',
                      'BIRTHDAY': '//span[contains(text(),"Сегодня родились")]',
                      'SELECTIONS': '//span[contains(text(),"Рейтинги")]',
                     }

    STARS_DROPDOWN_URLS = {'ARTICLES': BASE_URL + 'msk/stars/articles/',
                           'BIRTHDAY': BASE_URL + 'person/birthday/',
                           'SELECTIONS': BASE_URL + 'stars/selections/',
                          }

    # nav bar buttons
    def click_cinema(self):
        self.click(self.CINEMA_BUTTON)

    def click_series(self):
        self.click(self.SERIES_BUTTON)

    def click_tvshow(self):
        self.click(self.TVSHOW_BUTTON)

    def click_tv(self):
        self.click(self.TV_BUTTON)

    def click_stars(self):
        self.click(self.STARS_BUTTON)

    # cinema dropdown buttons
    def click_kinoafisha(self):
        self.hover(self.CINEMA_BUTTON)
        self.click(self.CINEMA_DROPDOWN['KINOAFISHA'])

    def click_cinema_online(self):
        self.hover(self.CINEMA_BUTTON)
        self.click(self.CINEMA_DROPDOWN['ONLINE'])

    def click_cinema_top(self):
        self.hover(self.CINEMA_BUTTON)
        self.click(self.CINEMA_DROPDOWN['TOP'])

    def click_cinema_soon(self):
        self.hover(self.CINEMA_BUTTON)
        self.click(self.CINEMA_DROPDOWN['SOON'])

    def click_cinema_selections(self):
        self.hover(self.CINEMA_BUTTON)
        self.click(self.CINEMA_DROPDOWN['SELECTIONS'])

    def click_cinema_awards(self):
        self.hover(self.CINEMA_BUTTON)
        self.driver.implicitly_wait(1)
        self.click(self.CINEMA_DROPDOWN['AWARDS'])

    def click_cinema_places(self):
        self.hover(self.CINEMA_BUTTON)
        self.driver.implicitly_wait(1)
        self.click(self.CINEMA_DROPDOWN['PLACES'])

    def click_cinema_articles(self):
        self.hover(self.CINEMA_BUTTON)
        self.driver.implicitly_wait(1)
        self.click(self.CINEMA_DROPDOWN['ARTICLES'])

    # series dropdown buttons
    def click_series_top(self):
        self.hover(self.SERIES_BUTTON)
        self.click(self.SERIES_DROPDOWN['TOP'])

    def click_series_online(self):
        self.hover(self.SERIES_BUTTON)
        self.click(self.SERIES_DROPDOWN['ONLINE'])

    def click_series_selections(self):
        self.hover(self.SERIES_BUTTON)
        self.click(self.SERIES_DROPDOWN['SELECTIONS'])

    def click_series_all(self):
        self.hover(self.SERIES_BUTTON)
        self.click(self.SERIES_DROPDOWN['ALL'])

    def click_series_articles(self):
        self.hover(self.SERIES_BUTTON)
        self.click(self.SERIES_DROPDOWN['ARTICLES'])

    # tvshow dropdown buttons
    def click_tvshow_top(self):
        self.hover(self.TVSHOW_BUTTON)
        self.click(self.TVSHOW_DROPDOWN['TOP'])

    def click_tvshow_online(self):
        self.hover(self.TVSHOW_BUTTON)
        self.click(self.TVSHOW_DROPDOWN['ONLINE'])

    def click_tvshow_all(self):
        self.hover(self.TVSHOW_BUTTON)
        self.click(self.TVSHOW_DROPDOWN['ALL'])

    def click_tvshow_articles(self):
        self.hover(self.TVSHOW_BUTTON)
        self.click(self.TVSHOW_DROPDOWN['ARTICLES'])

    # tvprogramm dropdown buttons
    def click_tv_central(self):
        self.hover(self.TV_BUTTON)
        self.click(self.TV_DROPDOWN['CENTRAL'])

    def click_tv_local(self):
        self.hover(self.TV_BUTTON)
        self.click(self.TV_DROPDOWN['LOCAL'])

    def click_tv_sport(self):
        self.hover(self.TV_BUTTON)
        self.click(self.TV_DROPDOWN['SPORT'])

    def click_tv_movies_and_series(self):
        self.hover(self.TV_BUTTON)
        self.click(self.TV_DROPDOWN['MOVIES_SERIES'])

    def click_tv_news(self):
        self.hover(self.TV_BUTTON)
        self.click(self.TV_DROPDOWN['NEWS'])

    # stars dropdown buttons
    def click_stars_articles(self):
        self.hover(self.STARS_BUTTON)
        self.click(self.STARS_DROPDOWN['ARTICLES'])

    def click_stars_birthday(self):
        self.hover(self.STARS_BUTTON)
        self.click(self.STARS_DROPDOWN['BIRTHDAY'])

    def click_stars_selections(self):
        self.hover(self.STARS_BUTTON)
        self.click(self.STARS_DROPDOWN['SELECTIONS'])
