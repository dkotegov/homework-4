import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component
from tests.utils import Constants


class AddPhotoButton(Component):
    INPUT_FOR_UPLOAD = '//input[@name="photo"]'
    CONFIRM_FILE_UPLOADING = '//div[@class="photo-sc __self uploading-album"]'

    def upload_file(self, filename):
        self.driver.find_element_by_xpath(self.INPUT_FOR_UPLOAD).send_keys(Constants.RESOURCES_PATH + filename)

    def check_upload_start_successfully(self):
        try:
            WebDriverWait(self.driver, 4, 0.5).until(
                lambda d: d.find_element_by_xpath(self.CONFIRM_FILE_UPLOADING)
            )
        except NoSuchElementException:
            return False
        return True
