# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.likes.components import *


class FriendsFeed(Page):

    def checkout(self):
        FriendsFeedButton(self.driver).click()
        FeedPhoto(self.driver).click()
        counter = PhotoLikeCounter(self.driver)
        assert(counter.is_empty())
        like_btn = PhotoLikeButton(self.driver)
        like_btn.click_disabled()
        assert (counter.count() == 1)
        like_btn.click_active()
        assert(counter.is_empty())
