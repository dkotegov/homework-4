from steps.default import DefaultSteps
from pages.file_preview import FilePreviewPage

import time

class PreviewFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = FilePreviewPage(driver)

    def upload_test_files(self):
        self.page.open()
        self.page.click_on_close_notion()

        files = [
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.jpeg',
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.jpg',
            '/Users/ivankovalenko/PycharmProjects/qa/homework-4/Чистая вода.png',
        ]

        for file in files:
            self.page.click_on_upload()
            self.page.upload_file(file)

