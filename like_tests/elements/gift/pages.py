# -*- coding: utf-8 -*-

from urlparse import urljoin
from like_tests.elements.page import Page
from like_tests.elements.like.components import *


class OwnGiftsPage(Page):

    def __init__(self, driver, path='gifts/received'):
        super(OwnGiftsPage, self).__init__(driver, path)

    def add_like(self):
        self.like_button.click_disabled(True)

    def remove_like(self):
        self.like_button.click_active(True)

    def likes_empty(self):
        return self.like_counter.is_empty()

    def likes_count(self):
        return self.like_counter.non_zero_count()

    @property
    def like_button(self):
        return GiftLikeButton(self.driver)

    @property
    def like_counter(self):
        return GiftLikeCounter(self.driver)


class FriendGiftsPage(OwnGiftsPage):

    def __init__(self, driver, user_path):
        super(FriendGiftsPage, self).__init__(driver, urljoin(user_path + '/', 'giftsFriend'))