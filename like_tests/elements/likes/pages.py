# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.likes.components import *


class FriendsFeed(Page):
    ACTIVE = FeedPhotoLikeButton.ACTIVE
    DISABLED = FeedPhotoLikeButton.DISABLED

    def open_photo(self):
        FriendsFeedButton(self.driver).click()
        FeedPhoto(self.driver).click()

    def add_like(self):
        self.like_button.click_disabled()

    def remove_like(self):
        self.like_button.click_active()

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, self.ACTIVE, self.DISABLED)

    @property
    def like_button(self):
        return FeedPhotoLikeButton(self.driver)
