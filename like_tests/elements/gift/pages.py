# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.like.components import *


class OwnGiftsPage(Page):
    PATH = 'gifts/received'

    def add_like(self):
        GiftLikeButton(self.driver).click_disabled()
        import time
        time.sleep(2)
        GiftLikeButton(self.driver).click_active()

