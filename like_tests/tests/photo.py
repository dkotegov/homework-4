# -*- coding: utf-8 -*-

from like_tests.tests.base import BasePhotoTest
from like_tests.elements.like.pages import FriendsFeed, OwnGeneralFeed


class LikePhotoTests(BasePhotoTest):

    def test_like_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        photo = feed.open_photo()
        self.assertTrue(photo.like_counter.is_empty())
        photo.add_like()
        self.assertEqual(photo.like_counter.non_zero_count(), 1)

    def test_remove_like_feed(self):
        self.user_page.logout()
        self.user_page.login_2()
        feed = FriendsFeed(self.driver)
        photo = feed.open_photo()
        photo.add_like()
        photo.remove_like()
        self.assertTrue(photo.like_counter.is_empty())

    def test_like_album_photo(self):
        self.photo_page.open()
        self.assertTrue(self.photo_page.like_counter.is_empty())
        self.photo_page.add_like()
        self.assertEqual(self.photo_page.like_counter.non_zero_count(), 1)

    def test_remove_like_album_photo(self):
        self.photo_page.open()
        self.photo_page.add_like()
        self.photo_page.remove_like()
        self.assertTrue(self.photo_page.like_counter.is_empty())

    def test_like_deleted_photo(self):
        self.user_page.open()
        self.user_page.open_own_feed()
        feed = OwnGeneralFeed(self.driver)
        photo = feed.open_photo()
        photo.delete()
        self.photo_deleted = True
        photo.close()
        feed.add_like()
        self.assertTrue(feed.like_counter.is_empty())

    def test_fast_likes(self):
        self.photo_page.open()
        self.driver.implicitly_wait(0.5)
        for i in range(0, 10):
            self.photo_page.add_like(True)
            self.photo_page.remove_like(True)
        self.assertTrue(self.photo_page.like_counter.is_empty())

    def test_class_identical(self):
        self.photo_page.open()
        self.photo_page.add_like()
        self.user_page.open()
        self.user_page.open_own_feed()
        feed = OwnGeneralFeed(self.driver)
        photo = feed.open_photo()
        self.assertEqual(photo.like_counter.non_zero_count(), 1)
