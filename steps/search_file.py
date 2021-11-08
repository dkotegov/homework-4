import os

from steps.default import DefaultSteps
from pages.search_file import SearchFilePage

class SearchFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = SearchFilePage(driver)

    def load_test_file(self, filename):
        self.page.open()
        self.page.click_on_close_notion()
        self.page.click_on_upload()
        self.page.upload_file(os.getcwd() + '/assets/' + filename)
        self.page.wait_popup_to_close()

    def search_empty_string(self):
        self.page.open()
        self.page.click_on_input()
        self.page.remove_input()
        self.page.click_on_search_button()

    def search_uploaded_file(self, filename):
        self.page.open()
        self.page.click_on_input()
        self.page.remove_input()
        self.page.set_filename(filename)
        self.page.click_on_search_button()

    def search_uploaded_file_with_type(self, filename, search_type):
        self.page.open()
        self.page.select_search_type(search_type)
        self.page.click_on_input()
        self.page.remove_input()
        self.page.set_filename(filename)
        self.page.click_on_search_button()

    def search_nonexistent_file_with_type(self, filename, search_type):
        self.page.open()
        self.page.select_search_type(filename)
        self.page.click_on_input()
        self.page.remove_input()
        self.page.set_filename(search_type)
        self.page.click_on_search_button()

    def select_search_type(self, search_type):
        self.page.open()
        self.page.open_dropdown_search_types()
        self.page.select_search_type(search_type)

    def check_search_result_is_empty(self):
        return self.page.check_search_result_is_empty()

    def check_search_file_is_found(self, filename):
        return self.page.check_search_file_is_found(filename)

    def check_selected_type(self, search_type):
        return self.page.check_selected_type(search_type)
