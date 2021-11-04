import time

from steps.default import DefaultSteps
from pages.hover_over_file import HoverOverFilePage

class HoverOverFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = HoverOverFilePage(driver)

    def add_to_favorites_first_file(self):
        self.page.open_alternative(self.page.FAV_SECTION)
        self.page.get_favorites()
        self.page.open()
        self.page.add_to_favorites_first_file()

    def check_file_in_favorites(self):
        self.page.open_alternative(self.page.FAV_SECTION)
        return self.page.check_item_in_favorites()

    def remove_first_file_from_favorites(self):
        self.page.open_alternative(self.page.FAV_SECTION)
        self.page.get_favorites()
        self.page.open()
        self.page.remove_first_file_from_favorites()

    def download_first_file(self):
        self.page.open()
        self.page.download_first_file()

    def check_file_downloaded(self):
        return self.page.check_file_downloaded()