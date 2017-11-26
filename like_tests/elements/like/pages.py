# -*- coding: utf-8 -*-

from like_tests.elements.photo.pages import *
from like_tests.elements.like.components import *


class FriendsFeed(Page):

    def open_feed(self):
        FriendsFeedButton(self.driver).click()

    def open_photo(self):
        self.open_feed()
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return FeedPhotoPage(self.driver)

    def add_like(self):
        self.like_button.click_disabled()

    def remove_like(self):
        self.like_button.click_active()

    @property
    def like_button(self):
        return CompactPhotoLikeButton(self.driver)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, CompactPhotoLikeButton.ACTIVE, CompactPhotoLikeButton.DISABLED)


class OwnGeneralFeed(Page):

    def open_photo(self):
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return OwnPhotoPage(self.driver)

    def add_like(self):
        self.like_button.click_disabled()

    @property
    def like_button(self):
        return CompactPhotoLikeButton(self.driver)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, CompactPhotoLikeButton.ACTIVE, CompactPhotoLikeButton.DISABLED)
