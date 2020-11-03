from Base import Page
from Favorites.FavoritesComponents import *


class FavoritePage(Page):
    PATH = 'favorites/'

    @property
    def utils(self):
        return Utils(self.driver)
