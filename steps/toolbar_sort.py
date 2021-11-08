import time

from steps.default import DefaultSteps
from pages.toolbar_sort import ToolbarSortFilesPage

class ToolbarSortFiles(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = ToolbarSortFilesPage(driver)

    def sort_by_alphabet_asc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_date() # We do this because alphabetic order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_alphabetic()

    def sort_by_alphabet_desc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_date()  # We do this because alphabetic order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_alphabetic()
        self.page.click_sort_dropdown()
        self.page.click_sort_alphabetic()

    def sort_by_size_asc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_date()  # We do this because size order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_size()

    def sort_by_size_desc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_date()  # We do this because size order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_size()
        self.page.click_sort_dropdown()
        self.page.click_sort_size()

    def sort_by_date_asc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_alphabetic()  # We do this because date order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_date()

    def sort_by_date_desc(self):
        # self.page.open_alternative(self.page.PATH + '/' + self.page.SORT_DIR)
        self.page.open()
        self.page.click_sort_dropdown()
        self.page.click_sort_alphabetic()  # We do this because date order may be already installed

        self.page.click_sort_dropdown()
        self.page.click_sort_date()
        self.page.click_sort_dropdown()
        self.page.click_sort_date()


    def check_correct_order(self, correct_order):
        self.page.get_all_files()
        all_files_names = [sorted_file.split('/')[-1] for sorted_file in self.page.ALL_FILES]
        return correct_order == all_files_names
