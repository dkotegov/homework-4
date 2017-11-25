# -*- coding: utf-8 -*-

from like_tests.elements.component import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class PhotoUploadButton(Component):
    BUTTON = '//input[@type="file"][@name="photo"]'
    SELECTABLE_ICON = '//span[@class="selectable-card_ic"]'

    def load_photo(self, photo_path):
        self.driver.find_element_by_xpath(self.BUTTON).send_keys(photo_path)
        self.driver.find_element_by_xpath(self.SELECTABLE_ICON)


class AvatarUploadButton(Clickable):
    CLICK = '//div[@class="stub-img stub-img__288 stub-img__user-change288"]'


class AvatarSelection(Clickable):
    CLICK = '//div[@class="photo-crop"]/a'


class UserAlbumButton(Clickable):
    CLICK = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'


class AlbumPhoto(Component):
    PHOTO = '//a[@class="photo-card_cnt"]'

    @property
    def reference(self):
        return self.driver.find_element_by_xpath(self.PHOTO)

    @property
    def url(self):
        return WebDriverWait(
            self.driver,
            self.TIMEOUT,
            self.POLL_FREQUENCY,
            ignored_exceptions=StaleElementReferenceException
        ).until(
            lambda d: d.find_element_by_xpath(self.PHOTO).get_attribute('href')
        )


class PhotoDeleteButton(Clickable):
    CLICK = '//a[descendant::i[@class="tico_img ic ic_delete"]]'


class PhotoCloseButton(Clickable):
    CLICK = '//div[@class="js-photoLayerClose ic photo-layer_close"]'
