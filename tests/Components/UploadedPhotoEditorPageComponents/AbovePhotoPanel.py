from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component


class AbovePhotoPanel(Component):
    CONFIRM_PHOTO_UPLOADED = '//li[@id="uploadingCompleteMsg"]'
    CANCEL_PHOTO_UPLOADING_LINK = '//li[@id="abortUploadingLink"]'
    CONFIRM_PHOTO_UPLOADING_CANCELED = '//li[@id="uploadingAbortedMsg"]'

    def wait_until_photo_will_be_downloaded(self):
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PHOTO_UPLOADED)
        )

    def cancel_photo_uploading(self):
        self.driver.find_element_by_xpath(self.CANCEL_PHOTO_UPLOADING_LINK)

    def wait_until_uploading_canceled(self):
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PHOTO_UPLOADING_CANCELED)
        )
