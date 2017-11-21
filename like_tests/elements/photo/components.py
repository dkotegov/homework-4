# -*- coding: utf-8 -*-

from like_tests.elements.component import Component


class PhotoUploadButton(Component):
    BUTTON = '//input[@type="file"][@name="photo"]'
    ALBUM = '//a[@hrefattrs="st.cmd=userPersonalPhotos"]'
    PHOTO = '//a[@class="photo-card_cnt"][@href!="{}"]'
    MOVE_PANEL = '//a[@data-l="aid,PhotoUpload_ShowMovePanel"]'

    def load_photo(self, photo_path):
        self.driver.find_element_by_xpath(self.BUTTON).send_keys(photo_path)
        self.driver.find_element_by_xpath(self.MOVE_PANEL)