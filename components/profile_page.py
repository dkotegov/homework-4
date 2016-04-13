# -*- coding: utf-8 -*-

import urlparse

from components.component import *


class MainHeader(Component):
    BASE_URL = 'https://afisha.mail.ru/'
    BASE_TV_URL = 'https://tv.mail.ru/'

    SUBHEADERS = {'CINEMA': '//span[text()="Фильмы"]', 'SERIES': '//span[text()="Сериалы"]',
                  'TV_SHOWS': '//span[text()="Телешоу"]', 'TV_PROGRAM': '//span[text()="Телепрограмма"]',
                  'STARS': '//span[text()="Звёзды"]'}

    CINEMA_LINKS = 'msk/cinema/'
    SERIES_LINKS = 'msk/series/'
    TV_SHOWS_LINKS = 'msk/tvshow/'
    TV_PROGRAM_LINKS = 'moskva/'
    STARS_LINKS = 'stars/'

    def __init__(self, driver):
        super(MainHeader, self).__init__(driver)

        def make_link(base, obj):
            return urlparse.urljoin(base, obj)

        self.cinema_href = make_link(self.BASE_URL, self.CINEMA_LINKS)
        self.series_href = make_link(self.BASE_URL, self.SERIES_LINKS)
        self.shows_href = make_link(self.BASE_URL, self.TV_SHOWS_LINKS)
        self.programs_href = make_link(self.BASE_TV_URL, self.TV_PROGRAM_LINKS)
        self.stars_href = make_link(self.BASE_URL, self.STARS_LINKS)

    def click_subheader(self, obj):
        return self.click(self.SUBHEADERS[obj])

    def hover_subheader(self, obj):
        return self.hover(self.SUBHEADERS[obj])


class LinksHeader(Component):
    pass


class BioBlock(Component):
    pass


class ErrorBlock(Component):
    pass


class CinemaBlock(Component):
    pass


class NewsBlock(Component):
    pass


class ReviewBlock(Component):
    pass
