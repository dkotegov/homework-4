# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.likes.components import *


class FriendsFeed(Page):
    ACTIVE = FeedPhotoLikeButton.ACTIVE
    DISABLED = FeedPhotoLikeButton.DISABLED

    def open_photo(self):
        FriendsFeedButton(self.driver).click()
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return FeedPhotoPage(self.driver, self.ACTIVE, self.DISABLED)


class OwnGeneralFeed(Page):
    ACTIVE = OwnPhotoLikeButton.ACTIVE
    DISABLED = OwnPhotoLikeButton.DISABLED

    def open_photo(self):
        FeedPhotoIcon(self.driver).click()
        FeedPhotoLikeButtonBig(self.driver).find()
        return FeedPhotoPage(self.driver, self.ACTIVE, self.DISABLED)

    def add_like(self):
        self.like_button.click_disabled()

    @property
    def like_button(self):
        return OwnPhotoLikeButton(self.driver)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED)


class FeedPhotoPage(Clickable):
    def __init__(self, driver, active, disabled):
        super(FeedPhotoPage, self).__init__(driver)
        self.ACTIVE = active
        self.DISABLED = disabled

    def add_like(self, wait_for_completion=False):
        self.like_button.click_disabled(wait_for_completion)

    def remove_like(self, wait_for_completion=False):
        self.like_button.click_active(wait_for_completion)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED)

    @property
    def like_button(self):
        return FeedPhotoLikeButton(self.driver)
