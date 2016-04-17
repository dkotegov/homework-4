# -*- coding: utf-8 -*-

from components.common_blocks import *
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


"""
class ActorProfilePage(BasePage):
    PATH = 'person/471877_sasha_grey/'

    def __init__(self, driver):
        super(ActorProfilePage, self).__init__(driver)

    @property
    def main_header(self):
        return MainHeader(self.driver)

    @property
    def link_header(self):
        return LinksHeader(self.driver)

    @property
    def bio_block(self):
        return BioBlock(self.driver)

    @property
    def error_block(self):
        return ErrorBlock(self.driver)

    @property
    def cinema_block(self):
        return CinemaBlock(self.driver)

    @property
    def news_block(self):
        return NewsBlock(self.driver)

    @property
    def review_block(self):
        return ReviewBlock(self.driver)
"""
