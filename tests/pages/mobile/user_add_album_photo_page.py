# -*- coding: utf-8 -*-
from os.path import abspath

from tests.pages.mobile.page import Page, Component
from tests.utils.waits import wait_until_url_changes


class UserAddAlbumPhotoPage(Page):
    PATH = '/dk?st.cmd=userAddAlbumPhoto&st.albId={}'

    def __init__(self, driver, album_id=None):
        super().__init__(driver)
        self.album_id = album_id

    @property
    def form(self):
        return AddPhotoForm(self.driver)

    def open(self, path=None):
        if path is None:
            path = self.PATH.format(self.album_id)
        super().open(path)

    def upload_photo(self, photo=abspath('tests/photos/test_photo.jpg')):
        self.open()
        self.form.upload_photo(photo)


class AddPhotoForm(Component):
    FORM = 'photo_upload_form'
    FILE_INPUT = 'field_file'
    UPLOAD_PHOTO_BUTTON = 'upload_photo_btn'
    EDIT_ALBUM_PHOTO_URL = 'st.cmd=userEditAlbumPhoto'
    ERROR = '//label[@id="field_file_label" and @role="alert"]'

    @wait_until_url_changes
    def upload_photo(self, photo):
        self.driver.execute_script("arguments[0].className=''", self.driver.find_element_by_id(self.FILE_INPUT))
        file_input = self.driver.find_element_by_id(self.FILE_INPUT)
        file_input.send_keys(photo)
        self.driver.execute_script("arguments[0].submit()", self.driver.find_element_by_id(self.FORM))

    @property
    def is_error(self):
        try:
            return self.driver.find_element_by_xpath(self.ERROR)
        except:
            return False
