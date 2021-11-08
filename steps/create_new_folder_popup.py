import time

from steps.default import DefaultSteps
from pages.create_new_folder_popup import CreateNewFolderPopupPage

class CreateNewFolderPopup(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = CreateNewFolderPopupPage(driver)

    def create_new_folder(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.click_on_submit()

    def create_new_shared_folder(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.click_on_submit_shared()

    def create_new_folder_empty_name(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.remove_input()
        self.page.click_on_submit()

    def create_new_shared_folder_empty_name(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.remove_input()
        self.page.click_on_submit_shared()

    def create_new_folder_long_name(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.long_input()
        self.page.click_on_submit()

    def create_new_shared_folder_long_name(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_folder()
        self.page.long_input()
        self.page.click_on_submit_shared()

    def errorExists(self):
        return self.page.checkErrorExists()