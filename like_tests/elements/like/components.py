# -*- coding: utf-8 -*-

from like_tests.elements.component import *


class FriendsFeedButton(Clickable):
    CLICK = '//div[@class="main-feed portlet"]//a[text()[contains(., "Друзья")]]'


class PostPhoto(Clickable):
    CLICK = '//div[@class="media-block media-photos "]//a'
