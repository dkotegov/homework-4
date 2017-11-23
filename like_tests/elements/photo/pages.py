# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.photo.components import *


class AlbumPage(Page):

    def __init__(self, driver):
        super(AlbumPage, self).__init__(driver)
        self.url = None

    def load_photo(self, path):
        PhotoUploadButton(self.driver).load_photo(path)
        UserAlbumButton(self.driver).click()
        self.url = Photo(self.driver).url
        return self

    def update_avatar(self):
        AvatarUploadButton(self).click()


class PhotoPage(Page):

    def __init__(self, driver, photo_url):
        super(PhotoPage, self).__init__(driver)
        self.PATH = photo_url

    def delete_photo(self):
        PhotoDeleteButton(self.driver).click()