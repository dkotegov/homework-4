# -*- coding: utf-8 -*-


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class MainHeader(Component):
    pass


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
