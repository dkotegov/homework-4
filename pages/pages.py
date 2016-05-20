# -*- coding: utf-8 -*-

from components.common_blocks import MainHeader, NavBar, Footer
from components.favorites_page import FavoritesBlock
from components.awards_page import AwardsBlock
from components.profile_page import ProfileBlock
from components.ratings_page import RatingsBlock
from components.birth_page import BirthListBlock, BirthHeaderBlock
from components.film_page import FilmBlock
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


class FavoritesPage(BasePage):
    PATH = 'user/favorites/'

    @property
    def fav_block(self):
        return FavoritesBlock(self.driver)


class AwardsPage(BasePage):
    PATH = 'awards/'

    @property
    def awards_block(self):
        return AwardsBlock(self.driver)


class ProfilePage(BasePage):
    PATH = 'person/471877_sasha_grey/'

    @property
    def profile_block(self):
        return ProfileBlock(self.driver)


class RatingsPage(BasePage):
    PATH = 'user/ratings/cinema/'

    @property
    def ratings_block(self):
        return RatingsBlock(self.driver)


class BirthPage(BasePage):
    PATH = 'person/birthday/'

    @property
    def header_block(self):
        return BirthHeaderBlock(self.driver)

    @property
    def user_list_block(self):
        return BirthListBlock(self.driver)


class FilmPage(BasePage):
    PATH = 'cinema/movies/722376_serbskij_film/'

    def refresh(self):
        self.driver.refresh()

    @property
    def film_block(self):
        return FilmBlock(self.driver)
