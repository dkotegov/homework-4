#!/usr/bin/env python2

import sys
import unittest
from margarita.tests.virusmusic.tracks.track_like_test import TrackLikeTest
from margarita.tests.virusmusic.tracks.track_like_test import TrackLikeTestNoAuth
from margarita.tests.virusmusic.tracks.track_add_playlist_test import TrackAddAndRemoveFromPlaylistTest
from margarita.tests.virusmusic.tracks.track_add_playlist_test import TrackAddToPlaylistTestNoAuth

from margarita.tests.virusmusic.player.player_queue_tests import TrackPlayTest, TrackRemoveFromQueueTest, \
    TrackPlayFromQueueTest, \
    TrackNextQueueTest, TrackPrevQueueTest, ShuffleQueueTest, CycleQueueTest

from margarita.tests.virusmusic.player.player_wrap_test import TestWrapPlayer


def run_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(TrackLikeTest),
        unittest.makeSuite(TrackLikeTestNoAuth),
        unittest.makeSuite(TrackAddAndRemoveFromPlaylistTest),
        unittest.makeSuite(TrackAddToPlaylistTestNoAuth),
        unittest.makeSuite(TrackPlayTest),
        unittest.makeSuite(TrackRemoveFromQueueTest),
        unittest.makeSuite(TrackPlayFromQueueTest),
        unittest.makeSuite(TrackNextQueueTest),
        unittest.makeSuite(TrackPrevQueueTest),
        unittest.makeSuite(TestWrapPlayer),
        unittest.makeSuite(ShuffleQueueTest),
        unittest.makeSuite(CycleQueueTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
