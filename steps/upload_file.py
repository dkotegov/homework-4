from steps.default import DefaultSteps
from pages.upload_file_popup import UploadFilePopupPage

import time

class UploadFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = UploadFilePopupPage(driver)

    def upload_file(self, file_path):
        self.page.open()
        try:
            self.page.click_on_close_notion()
        except:
            pass
        self.page.click_on_upload()
        self.page.upload_file(file_path)

    def upload_files(self, files):
        self.page.open()
        try:
            self.page.click_on_close_notion()
        except:
            pass
        self.page.click_on_upload()
        for file in files:
            self.page.upload_file(file)
            time.sleep(1)

    def error_exists(self):
        return self.page.check_error_exists()

    def click_remove_the_restriction(self):
        self.page.open()
        self.page.click_on_close_notion()
        self.page.click_on_upload()
        self.page.click_remove_the_restriction()
