from Base import Page
from Home.HomeComponents import *


class HomePage(Page):
    PATH = 'home/'

    def open(self):
        super(HomePage, self).open()
        self.utils.close_banner_if_exists()

    @property
    def utils(self):
        return Utils(self.driver)

    @property
    def folders(self):
        return Folders(self.driver)
