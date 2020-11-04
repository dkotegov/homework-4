from Base import Page
from TrashBin.TrashBinComponents import *
from Home.HomeComponents import Utils as HomeUtils


class TrashBinPage(Page):
    PATH = 'trashbin/'

    @property
    def utils(self):
        return Utils(self.driver)

    @property
    def restore(self):
        return Restore(self.driver)

    @property
    def delete(self):
        return Delete(self.driver)

    @property
    def home_utils(self):
        return HomeUtils(self.driver)
