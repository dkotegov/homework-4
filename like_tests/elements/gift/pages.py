# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.like.components import *


class OwnGiftsPage(Page):

    def __init__(self, driver):
        super(OwnGiftsPage, self).__init__(driver, 'gifts/received')

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