import time

from steps.default import DefaultSteps
from pages.file_dropdown_menu import FileDropDownMenuPage

class FileDropDownMenu(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = FileDropDownMenuPage(driver)

    def open_first_file_in_new_tab(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.open_in_new_tab()
        self.page.switch_to_nth_tab(1)

    def send_via_male(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.send_via_male()
        self.page.switch_to_nth_tab(1)

    def add_to_favorites(self):
        self.page.open_alternative(self.page.FAV_SECTION)
        self.page.get_favorites()
        self.page.open()
        self.page.right_click_on_non_fav_item()
        self.page.click_add_to_favorites()

    def rename_file_with_empty_string(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.click_rename()
        self.page.remove_rename_input()
        self.page.click_submit()


    def rename_file_with_long_string(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.click_rename()
        self.page.input_long_string()
        self.page.click_submit()

    def download_first_file(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.click_download()

    def open_modal_remove(self):
        self.page.open()
        self.page.right_click_first_file()
        self.page.click_remove()

    def move_file_to_bin(self):
        self.open_modal_remove()
        self.page.click_submit()

    def close_modal_remove(self):
        self.page.close_modal_remove()

    def check_file_in_bin(self):
        self.page.open_alternative(self.page.BIN_SECTION)
        return self.page.check_remove_modal_exists()

    def check_modal_remove_exists(self):
        return self.page.check_remove_modal_exists()

    def compare_file_names(self, selector):
        return self.page.compare_file_names(selector)

    def check_item_in_favorites(self):
        self.page.open_alternative(self.page.FAV_SECTION)
        return self.page.check_item_in_favorites()

    def check_error_exists(self):
        return self.page.check_error_exists()

    def check_file_downloaded(self):
        return self.page.check_file_downloaded()
