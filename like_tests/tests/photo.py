# -*- coding: utf-8 -*-

from like_tests.tests.base import BasePhotoTest
from like_tests.elements.like.pages import *


class ClassPhotoTest(BasePhotoTest):

    def test_like_page_photo(self):
        self.user_page.open()
        self.user_page.logout()
        self.user_page.login_2()
        FriendsFeed(self.driver).checkout()
        assert(1 == 1)