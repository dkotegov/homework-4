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
    ACTIVE = PhotoLikeButton.ACTIVE
    DISABLED = PhotoLikeButton.DISABLED

    def __init__(self, driver, photo_url):
        super(PhotoPage, self).__init__(driver)
        self.PATH = photo_url

    def add_like_to_zero(self):
        PhotoLikeButton(self.driver).click_disabled()

    def has_empty_likes(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED).is_empty()

    def non_zero_likes(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED).non_zero_count()

    def remove_like(self):
        PhotoLikeButton(self.driver).click_active()

    def delete_photo(self):
        PhotoDeleteButton(self.driver).click()
