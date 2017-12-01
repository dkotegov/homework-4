# -*- coding: utf-8 -*-

import urlparse

from .base import AuthForm, Main, CreateAlbum, Album

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


class PhotoPage(Page):
    
    @property
    def open_photos(self):
        return Main(self.driver)

    @property
    def create_album(self):
        return CreateAlbum(self.driver)

    @property
    def album(self):
        return Album(self.driver)
