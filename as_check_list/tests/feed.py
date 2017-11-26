# -*- coding: utf-8 -*-

from as_check_list.tests.base import BasePhotoTest
from as_check_list.elements.like.pages import FriendsFeed


class FeedLikeTests(BasePhotoTest):
    def test_like_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        feed.open_feed()
        self.assertTrue(feed.like_counter.is_empty())
        feed.add_like()
        self.assertEqual(feed.like_counter.non_zero_count(), 1)

    def test_like_remove_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        feed.open_feed()
        feed.add_like()
        feed.remove_like()
        self.assertTrue(feed.like_counter.is_empty())
