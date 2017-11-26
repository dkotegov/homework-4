# -*- coding: utf-8 -*-

from as_check_list.tests.base import BaseGiftTest
from as_check_list.elements.gift.pages import OwnGiftsPage, FriendGiftsPage


# Предполагается, что у пользователя уже есть подарок
class GiftLikeTests(BaseGiftTest):
    def test_add_like(self):
        gift_page = OwnGiftsPage(self.driver)
        gift_page.open()
        gift_page.add_like()
        self.like_added = True
        self.assertEqual(gift_page.likes_count(), 1)

    def test_remove_like(self):
        gift_page = OwnGiftsPage(self.driver)
        gift_page.open()
        gift_page.add_like()
        self.like_added = True
        gift_page.remove_like()
        self.like_added = False
        self.driver.refresh()
        self.assertTrue(gift_page.likes_empty())

    def test_like_equal(self):
        gift_page = OwnGiftsPage(self.driver)
        gift_page.open()
        gift_page.add_like()
        self.like_added = True
        self.user_page.logout()
        self.user_page.login_2()
        friend_gifts_page = FriendGiftsPage(self.driver, self.user_page.USER_PATH1)
        friend_gifts_page.open()
        self.assertEqual(friend_gifts_page.likes_count(), 1)
