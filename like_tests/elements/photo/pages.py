# -*- coding: utf-8 -*-

from urlparse import urlparse, urljoin

from like_tests.elements.page import Page
from like_tests.elements.photo.components import *
from like_tests.elements.like.components import *


class AlbumPage(Page):
    def __init__(self, driver, user_path=''):
        super(AlbumPage, self).__init__(driver)
        self.PATH = urljoin(user_path, 'pphotos')

    @property
    def photo(self):
        return AlbumPhoto(self.driver)


class PhotoUploadPage(Page):
    def __init__(self, driver):
        super(PhotoUploadPage, self).__init__(driver)
        self.photo_url = None

    def load_photo(self, path):
        PhotoUploadButton(self.driver).load_photo(path)
        UserAlbumButton(self.driver).click()
        self.photo_url = AlbumPage(self.driver).photo.url
        return self


class OwnPhotoPage(Page):

    def __init__(self, driver, photo_url=''):
        super(OwnPhotoPage, self).__init__(driver)
        self.PATH = photo_url

    def add_like(self, wait_for_completion=False):
        self.like_button.click_disabled(wait_for_completion)

    def remove_like(self, wait_for_completion=False):
        self.like_button.click_active(wait_for_completion)

    def delete(self):
        self.delete_button.click()

    def close(self):
        self.close_button.click()

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, OwnPhotoLikeButton.ACTIVE, OwnPhotoLikeButton.DISABLED)

    @property
    def like_button(self):
        return OwnPhotoLikeButton(self.driver)

    @property
    def delete_button(self):
        return PhotoDeleteButton(self.driver)

    @property
    def close_button(self):
        return PhotoCloseButton(self.driver)


class FeedPhotoPage(Clickable):

    def add_like(self, wait_for_completion=False):
        self.like_button.click_disabled(wait_for_completion)

    def remove_like(self, wait_for_completion=False):
        self.like_button.click_active(wait_for_completion)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, FeedPhotoLikeButton.ACTIVE, FeedPhotoLikeButton.DISABLED)

    @property
    def like_button(self):
        return FeedPhotoLikeButton(self.driver)
