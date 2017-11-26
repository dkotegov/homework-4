# -*- coding: utf-8 -*-

from like_tests.tests.base import BaseTest
from like_tests.elements.gift.pages import OwnGiftsPage


class GiftLikeTests(BaseTest):

    def test_open(self):
        OwnGiftsPage(self.driver).open()
        import time
        OwnGiftsPage(self.driver).add_like()
        time.sleep(4)
        assert (1 == 1)
