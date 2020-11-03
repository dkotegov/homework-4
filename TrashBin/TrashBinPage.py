from Base import Page
from TrashBin.TrashBinComponents import *


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
