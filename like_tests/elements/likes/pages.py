# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.likes.components import *
from like_tests.elements.photo.pages import *


class FriendsFeed(Page):

    def open_photo(self):
        FriendsFeedButton(self.driver).click()
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return FeedPhotoPage(self.driver)


class OwnGeneralFeed(Page):

    def open_photo(self):
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return OwnPhotoPage(self.driver)

    def add_like(self):
        self.like_button.click_disabled()

    @property
    def like_button(self):
        return OwnPhotoLikeButton(self.driver)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, OwnPhotoLikeButton.ACTIVE, OwnPhotoLikeButton.DISABLED)



