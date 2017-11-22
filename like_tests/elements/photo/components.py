# -*- coding: utf-8 -*-

from like_tests.elements.component import Component


class PhotoUploadButton(Component):
    BUTTON = '//input[@type="file"][@name="photo"]'
    MOVE_PANEL = '//a[@data-l="aid,PhotoUpload_ShowMovePanel"]'

    def load_photo(self, photo_path):
        self.driver.find_element_by_xpath(self.BUTTON).send_keys(photo_path)
        self.driver.find_element_by_xpath(self.MOVE_PANEL)


class UserAlbumButton(Component):
    ALBUM = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'

    def click(self):
        self.driver.find_element_by_xpath(self.ALBUM).click()


class Photo(Component):
    PHOTO = '//a[contains(@class, "photo-card_cnt")]'

    @property
    def reference(self):
        return self.driver.find_element_by_xpath(self.PHOTO)

    @property
    def url(self):
        return self.reference.get_attribute('href')


class PhotoDeleteButton(Component):
    BUTTON = '//a[descendant::i[@class="tico_img ic ic_delete"]]'

    def click(self):
        self.driver.find_element_by_xpath(self.BUTTON).click()

