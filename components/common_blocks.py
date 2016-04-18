# -*- coding: utf-8 -*-

from components.component import *


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
    PASSWORD_INPUT = '//input[@id="ph_password"]'
    LOGIN_SUBMIT_BUTTON = '//span[@class="js-control js-control-login x-ph__button x-ph__button_action"]'

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
    TV_URL = 'https://tv.mail.ru/moskva/'
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


class Footer(Component):
    # 1st column
    CINEMA = '//a[@class="footer__menu__list__item__link" and contains(text(),"Фильмы")]'
    KINOAFISHA = '//a[@class="footer__menu__list__item__link" and contains(text(),"Киноафиша")]'
    CINEMA_ONLINE = '//a[@class="footer__menu__list__item__link" and contains(text(),"Фильмы онлайн")]'
    CINEMA_TOP = '//a[@class="footer__menu__list__item__link" and contains(text(),"Лучшие фильмы")]'
    SOON = '//a[@href="https://afisha.mail.ru/cinema/soon/#soon" and contains(text(),"Календарь кинопремьер")]'
    CINEMA_SELECTIONS = '//a[@class="footer__menu__list__item__link" and contains(text(),"Подборки")]'
    AWARDS = '//a[@class="footer__menu__list__item__link" and contains(text(),"Премии")]'
    PLACES = '//a[@class="footer__menu__list__item__link" and contains(text(),"Кинотеатры")]'
    CINEMA_ARTICLES = '//a[@class="footer__menu__list__item__link" and contains(text(),"Новости")]'

    def click_cinema(self):
        self.click(self.CINEMA)

    def click_kinoafisha(self):
        self.click(self.KINOAFISHA)

    def click_cinema_online(self):
        self.click(self.CINEMA_ONLINE)

    def click_cinema_top(self):
        self.click(self.CINEMA_TOP)

    def click_soon(self):
        self.click(self.SOON)

    def click_cinema_selections(self):
        self.click(self.CINEMA_SELECTIONS)

    def click_awards(self):
        self.click(self.AWARDS)

    def click_places(self):
        self.click(self.PLACES)

    def click_cinema_articles(self):
        self.click(self.CINEMA_ARTICLES)

    # 2nd column
    SERIES = '//a[@class="footer__menu__list__item__link" and contains(text(),"Сериалы")]'
    SERIES_TOP = '//a[@class="footer__menu__list__item__link" and contains(text(),"Лучшие сериалы")]'
    SERIES_ONLINE = '//a[@class="footer__menu__list__item__link" and contains(text(),"Сериалы онлайн")]'
    SERIES_SELECTIONS = '//a[@href="https://afisha.mail.ru/series/selections/" and contains(text(),"Подборки")]'
    SERIES_ALL = '//a[@class="footer__menu__list__item__link" and contains(text(),"Все сериалы")]'
    SERIES_ARTICLES = '//a[@href="https://afisha.mail.ru/msk/series/articles/" and contains(text(),"Новости")]'

    def click_series(self):
        self.click(self.SERIES)

    def click_series_top(self):
        self.click(self.SERIES_TOP)

    def click_series_online(self):
        self.click(self.SERIES_ONLINE)

    def click_series_selections(self):
        self.click(self.SERIES_SELECTIONS)

    def click_series_all(self):
        self.click(self.SERIES_ALL)

    def click_series_articles(self):
        self.click(self.SERIES_ARTICLES)

    # 3rd column
    TVSHOW = '//a[@class="footer__menu__list__item__link" and contains(text(),"Телешоу")]'
    TVSHOW_TOP = '//a[@class="footer__menu__list__item__link" and contains(text(),"Лучшие телешоу")]'
    TVSHOW_TOP_ONLINE = '//a[@class="footer__menu__list__item__link" and contains(text(),"Телешоу онлайн")]'
    TVSHOW_TOP_ALL = '//a[@class="footer__menu__list__item__link" and contains(text(),"Все телешоу")]'
    TVSHOW_TOP_ARTICLES = '//a[@href="https://afisha.mail.ru/msk/tvshow/articles/" and contains(text(),"Новости")]'

    def click_tvshow(self):
        self.click(self.TVSHOW)

    def click_tvshow_top(self):
        self.click(self.TVSHOW_TOP)

    def click_tvshow_top_online(self):
        self.click(self.TVSHOW_TOP_ONLINE)

    def click_tvshow_top_all(self):
        self.click(self.TVSHOW_TOP_ALL)

    def click_tvshow_top_articles(self):
        self.click(self.TVSHOW_TOP_ARTICLES)

    # 4th column
    TV = '//a[@class="footer__menu__list__item__link" and contains(text(),"Телепрограмма")]'
    TV_CENTRAL = '//a[@class="footer__menu__list__item__link" and contains(text(),"Центральные")]'
    TV_LOCAL = '//a[@class="footer__menu__list__item__link" and contains(text(),"Местные")]'
    TV_SPORT = '//a[@class="footer__menu__list__item__link" and contains(text(),"Спортивные")]'
    TV_MOVIES_SERIES = '//a[@class="footer__menu__list__item__link" and contains(text(),"Фильмы и Сериалы")]'
    TV_NEWS = '//a[@class="footer__menu__list__item__link" and contains(text(),"Новостные")]'

    def click_tv(self):
        self.click(self.TV)

    def click_tv_central(self):
        self.click(self.TV_CENTRAL)

    def click_tv_local(self):
        self.click(self.TV_LOCAL)

    def click_tv_sport(self):
        self.click(self.TV_SPORT)

    def click_tv_movies_series(self):
        self.click(self.TV_MOVIES_SERIES)

    def click_tv_news(self):
        self.click(self.TV_NEWS)

    # 5th column
    STARS = '//a[@class="footer__menu__list__item__link" and contains(text(),"Звёзды")]'
    STAR_ARTICLES = '//a[@class="footer__menu__list__item__link" and contains(text(),"Новости")]'
    STAR_BIRTHDAY = '//a[@class="footer__menu__list__item__link" and contains(text(),"Сегодня родились")]'
    STAR_SELECTIONS = '//a[@class="footer__menu__list__item__link" and contains(text(),"Рейтинги")]'

    def click_stars(self):
        self.click(self.STARS)

    def click_star_articles(self):
        self.click(self.STAR_ARTICLES)

    def click_star_birthday(self):
        self.click(self.STAR_BIRTHDAY)

    def click_star_selections(self):
        self.click(self.STAR_SELECTIONS)


    BASE_URL = 'https://afisha.mail.ru/'

    # 1st column
    CINEMA_URL = BASE_URL + 'msk/cinema/'
    KINOAFISHA_URL = BASE_URL + 'msk/cinema/kinoafisha/'
    CINEMA_ONLINE_URL = BASE_URL + 'cinema/online/'
    CINEMA_TOP_URL = BASE_URL + 'cinema/top/'
    SOON_URL = BASE_URL + 'cinema/soon/#soon'
    CINEMA_SELECTIONS_URL = BASE_URL + 'cinema/selections/'
    AWARDS_URL = BASE_URL + 'awards/'
    PLACES_URL = BASE_URL + 'msk/cinema/places/'
    CINEMA_ARTICLES_URL = BASE_URL + 'msk/cinema/articles/'

    # 2nd column
    SERIES_URL = BASE_URL + 'msk/series/'
    SERIES_TOP_URL = BASE_URL + 'series/top/'
    SERIES_ONLINE_URL = BASE_URL + 'series/online/'
    SERIES_SELECTIONS_URL = BASE_URL + 'series/selections/'
    SERIES_ALL_URL = BASE_URL + 'series/all/'
    SERIES_ARTICLES_URL = BASE_URL + 'msk/series/articles/'

    # 3rd column
    TVSHOW_URL = BASE_URL + 'msk/tvshow/'
    TVSHOW_TOP_URL = BASE_URL + 'tvshow/top/'
    TVSHOW_TOP_ONLINE_URL = BASE_URL + 'tvshow/online/'
    TVSHOW_TOP_ALL_URL = BASE_URL + 'tvshow/all/'
    TVSHOW_TOP_ARTICLES_URL = BASE_URL + 'msk/tvshow/articles/'

    # 4th column
    TV_BASE_URL = 'https://tv.mail.ru/'
    TV_URL = 'https://tv.mail.ru/moskva/'
    TV_CENTRAL_URL = TV_BASE_URL + 'moskva/central/'
    TV_LOCAL_URL = TV_BASE_URL + 'region/local/'
    TV_SPORT_URL = TV_BASE_URL + 'region/sport/'
    TV_MOVIES_SERIES_URL = TV_BASE_URL + 'region/movies_series/'
    TV_NEWS_URL = TV_BASE_URL + 'region/news/'

    # 5th column
    STARS_URL = BASE_URL + 'stars/'
    STAR_ARTICLES_URL = BASE_URL + 'msk/stars/articles/'
    STAR_BIRTHDAY_URL = BASE_URL + 'person/birthday/'
    STAR_SELECTIONS_URL = BASE_URL + 'stars/selections/'

