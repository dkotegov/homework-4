# -*- coding: utf-8 -*-

from components.common_blocks import *
from components.favorites_page import *
from components.awards_page import *
from components.profile_page import *
from components.ratings_page import *
import urlparse


class BasePage(object):
    BASE_URL = 'https://afisha.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def main_header(self):
        return MainHeader(self.driver)

    @property
    def nav_bar(self):
        return NavBar(self.driver)

    @property
    def footer(self):
        return Footer(self.driver)


class FavoritesPage(object):
    BASE_URL = 'https://afisha.mail.ru/'
    PATH = 'user/favorites/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def fav_block(self):
        return FavoritesBlock(self.driver)


class AwardsPage(object):
    BASE_URL = 'https://afisha.mail.ru/'
    PATH = 'awards/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def awards_block(self):
        return AwardsBlock(self.driver)


class ProfilePage(object):
    BASE_URL = 'https://afisha.mail.ru/'
    PATH = 'person/471877_sasha_grey/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def profile_block(self):
        return ProfileBlock(self.driver)


class RatingsPage(object):
    BASE_URL = 'https://afisha.mail.ru/'
    PATH = 'user/ratings/cinema/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def ratings_block(self):
        return RatingsBlock(self.driver)

