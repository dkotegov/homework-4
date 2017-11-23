# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.like.components import *


class FriendsFeed(Page):

    def checkout(self):
        FriendsFeedButton(self.driver).click()
        PostPhoto(self.driver).click()
