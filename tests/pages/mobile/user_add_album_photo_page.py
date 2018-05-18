# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component


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


class AddPhotoForm(Component):
    FORM = 'photo_upload_form'
    FILE_INPUT = 'field_file'
    UPLOAD_PHOTO_BUTTON = 'upload_photo_btn'
    EDIT_ALBUM_PHOTO_URL = 'st.cmd=userEditAlbumPhoto'

    def upload_photo(self, photo):
        self.driver.execute_script("document.getElementById('{}').className=''".format(self.FILE_INPUT))
        file_input = self.driver.find_element_by_id(self.FILE_INPUT)
        file_input.send_keys(photo)
        self.driver.execute_script("document.getElementById('{}').submit()".format(self.FORM))
        WebDriverWait(self.driver, 4).until(EC.url_contains(self.EDIT_ALBUM_PHOTO_URL))
