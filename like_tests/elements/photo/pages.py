# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.photo.components import *
from like_tests.elements.likes.components import *


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
    ACTIVE = PagePhotoLikeButton.ACTIVE
    DISABLED = PagePhotoLikeButton.DISABLED

    def __init__(self, driver, photo_url):
        super(PhotoPage, self).__init__(driver)
        self.PATH = photo_url

    def add_like(self):
        self.like_button.click_disabled()

    def remove_like(self):
        self.like_button.click_active()

    def delete_photo(self):
        self.delete_button.click()

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED)

    @property
    def like_button(self):
        return PagePhotoLikeButton(self.driver)

    @property
    def delete_button(self):
        return PhotoDeleteButton(self.driver)
