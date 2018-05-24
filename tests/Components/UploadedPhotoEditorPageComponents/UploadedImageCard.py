import re

from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component

from tests.utils import Constants
from tests.utils.Utils import Utils


class UploadedImageCard(Component):
    PHOTO_ID_DIV = '//div[@class="h-mod __uploaded"]'
    UPLOADED_PHOTO_SPAN = '//span[@class="photo-card_cnt"]'

    def get_uploaded_photo_id(self):
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda d: d.find_element_by_xpath(self.PHOTO_ID_DIV)
        )
        element = self.driver.find_element_by_xpath(self.PHOTO_ID_DIV)

        return element.get_attribute('data-id')

    def get_uploaded_photo_md5_check_sum(self):
        # get image source
        img = self.driver.find_element_by_xpath(self.UPLOADED_PHOTO_SPAN + '/img')
        src = img.get_attribute('src')

        # download the image
        utils = Utils
        utils.download_image(src, Constants.DOWNLOAD_IMAGE_NAME)

        # get md5 check sum
        return utils.md5(Constants.PROJECT_PATH + '/' + Constants.DOWNLOAD_IMAGE_NAME)
