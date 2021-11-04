from steps.default import DefaultSteps
from pages.toolbar import ToolbarPage
from steps.upload_file import UploadFile

import time

class Toolbar(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = ToolbarPage(driver)
        self.page.open()
        try:
            self.page.click_on_close_notion()
        except:
            pass
        upload_steps = UploadFile(driver)
        files = [
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.jpeg',
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.jpg',
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.png',
        ]
        try:
            upload_steps.upload_files(files)
        except:
            pass

    def select_all(self):
        self.page.open()
        try:
            self.page.click_on_close_notion()
        except:
            pass
        self.page.click_select_all()

    def download_all(self):
        self.page.open()
        self.page.click_on_close_notion()
        self.page.click_on_download()

    def all_items_selected(self):
        return self.page.all_items_selected()
