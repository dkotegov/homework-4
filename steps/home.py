from steps.default import DefaultSteps
from pages.toolbar import Toolbar

class HomeSteps(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = Toolbar(driver)

    def create_folder(self):
        self.page.open()
        self.page.click_on_create_something()
        self.page.click_on_create_folder()
        self.page.fill_create_new_folder_form("KEKW")
        self.page.create_new_folder_submit()

