# -*- coding: utf-8 -*-

from like_tests.elements.component import Component


class PhotoUploadButton(Component):
    # BUTTON = '//input[@class="html5-upload-link __before-upload"]'
    BUTTON = '//input[@type="file"][@name="photo"]'
    ALBUM = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'
    PHOTO = '//a[@class="photo-card_cnt"][@href!="{}"]'

    def load_photo(self, photo_path):
        self.driver.find_element_by_xpath(self.BUTTON).send_keys(photo_path)
        self.driver.find_element_by_xpath(self.ALBUM).click()
