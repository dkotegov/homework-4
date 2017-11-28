# -*- coding: utf-8 -*-

import urlparse

from .components import AuthForm, SearchField, Categories

class Page(object):
    BASE_URL = 'https://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    @property
    def form(self):
        return AuthForm(self.driver)  

class SearchPage(Page):
    PATH = 'search'

    @property
    def search_field(self):
        return SearchField(self.driver)

    @property
    def categories(self):
        return Categories(self.driver)
    