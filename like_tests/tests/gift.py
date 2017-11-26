# -*- coding: utf-8 -*-

from like_tests.tests.base import BaseTest
from like_tests.elements.gift.pages import OwnGiftsPage


class GiftLikeTests(BaseTest):

    def test_add_like(self):
        gift_page = OwnGiftsPage(self.driver)
        gift_page.open()
        gift_page.add_like()
        self.assertEqual(gift_page.likes_count(), 1)
        gift_page.remove_like()

    def test_remove_like(self):
        gift_page = OwnGiftsPage(self.driver)
        gift_page.open()
        gift_page.add_like()
        gift_page.remove_like()
        self.driver.refresh()
        self.assertTrue(gift_page.likes_empty())
