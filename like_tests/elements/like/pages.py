# -*- coding: utf-8 -*-

from like_tests.elements.page import Page
from like_tests.elements.like.components import *

import time


class FriendsFeed(Page):

    def checkout(self):
        FriendsFeedButton(self.driver).hard_click()
        PostPhoto(self.driver).click()
