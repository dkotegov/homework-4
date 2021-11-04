import time

from steps.default import DefaultSteps
from pages.toolbar_create_new_file import ToolbarCreateNewFilePage

class ToolbarCreateNewFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = ToolbarCreateNewFilePage(driver)

    def create_new_folder(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_create()
        self.page.click_folder()

    def create_new_docx(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_create()
        self.page.click_docx()

    def test_create_new_table(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_create()
        self.page.click_table()

    def test_create_new_presentation(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_create()
        self.page.click_presentation()

    def check_modal_exists(self):
        return self.page.check_modal_exists()