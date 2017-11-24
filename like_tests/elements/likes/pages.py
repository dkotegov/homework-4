# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.likes.components import *


class FriendsFeed(Page):

    def open_photo(self):
        FriendsFeedButton(self.driver).click()
        FeedPhoto(self.driver).click()

    def add_like(self):
        PhotoLikeButton(self.driver).click_disabled()

    def checkout(self):
        FriendsFeedButton(self.driver).click()
        FeedPhoto(self.driver).click()
        counter = PhotoLikeCounter(self.driver)
        assert(counter.is_empty())
        like_btn = PhotoLikeButton(self.driver)
        like_btn.click_disabled()
        assert (counter.non_zero_count() == 1)
        like_btn.click_active()
        assert(counter.is_empty())
