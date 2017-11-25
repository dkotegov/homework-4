# -*- coding: utf-8 -*-

from like_tests.tests.base import BasePhotoTest
from like_tests.elements.likes.pages import FriendsFeed, OwnGeneralFeed
from like_tests.elements.photo.pages import OwnPhotoPage


class LikePhotoTests(BasePhotoTest):

    def test_like_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        feed.open_photo()
        self.assertTrue(feed.like_counter.is_empty())
        feed.add_like()
        self.assertEqual(feed.like_counter.non_zero_count(), 1)

    def test_like_reset_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        feed.open_photo()
        feed.add_like()
        feed.remove_like()
        self.assertTrue(feed.like_counter.is_empty())

    def test_like_album_photo(self):
        self.photo_page.open()
        self.assertTrue(self.photo_page.like_counter.is_empty())
        self.photo_page.add_like()
        self.assertEqual(self.photo_page.like_counter.non_zero_count(), 1)

    def test_like_reset_album_photo(self):
        self.photo_page.open()
        self.photo_page.add_like()
        self.photo_page.remove_like()
        self.assertTrue(self.photo_page.like_counter.is_empty())

    def test_like_deleted_photo(self):
        self.user_page.open()
        self.user_page.user_header.click()
        feed = OwnGeneralFeed(self.driver)
        feed.open_photo()
        photo = OwnPhotoPage(self.driver, '')
        photo.delete()
        photo.close()
        feed.add_like()
        self.assertTrue(feed.like_counter.is_empty())
        self.photo_deleted = True

    def test_fast_likes(self):
        self.photo_page.open()
        self.driver.implicitly_wait(0.5)
        for i in range(0, 10):
            self.photo_page.add_like(True)
            self.photo_page.remove_like(True)
        self.assertTrue(self.photo_page.like_counter.is_empty())
