#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from as_check_list.tests.photo import LikePhotoTests
from as_check_list.tests.gift import GiftLikeTests
from as_check_list.tests.feed import FeedLikeTests


def as_tests():
    return [
        unittest.makeSuite(LikePhotoTests),
        unittest.makeSuite(GiftLikeTests),
        unittest.makeSuite(FeedLikeTests)
    ]
