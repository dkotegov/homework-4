from Base import Page
from Home.HomeComponents import *


class HomePage(Page):
    PATH = 'home/'

    @property
    def utils(self):
        return Utils(self.driver)

    @property
    def folders(self):
        return Folders(self.driver)
