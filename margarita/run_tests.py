#!/usr/bin/env python2

import sys
import unittest

from margarita.tests.todo.task.create_test import CreateTaskTest, CreateTaskSpacesTest, CreateTaskSymbolsTest
from margarita.tests.virusmusic.player.player_queue_tests import TrackPlayTest, TrackRemoveFromQueueTest, \
    TrackPlayFromQueueTest, TrackNextQueueTest, TrackPrevQueueTest, ShuffleQueueTest, CycleQueueTest
from margarita.tests.virusmusic.player.player_wrap_test import TestWrapPlayer
from margarita.tests.virusmusic.search.search_no_results import SearchNoResults
from margarita.tests.virusmusic.search.search_one_result_test import SearchArtistOneResultTest, \
    SearchAlbumOneResultTest, SearchTrackOneResultTest
from margarita.tests.virusmusic.search.search_tests import SearchArtistTest, SearchAlbumTest, SearchTrackTest, SearchAllResults
from margarita.tests.virusmusic.tracks.track_add_playlist_test import TrackAddAndRemoveFromPlaylistTest
from margarita.tests.virusmusic.tracks.track_like_test import TrackLikeTest


def run_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(TrackLikeTest),
        unittest.makeSuite(TrackAddAndRemoveFromPlaylistTest),
        unittest.makeSuite(TrackPlayTest),
        unittest.makeSuite(TrackRemoveFromQueueTest),
        unittest.makeSuite(TrackPlayFromQueueTest),
        unittest.makeSuite(TrackNextQueueTest),
        unittest.makeSuite(TrackPrevQueueTest),
        unittest.makeSuite(TestWrapPlayer),
        unittest.makeSuite(ShuffleQueueTest),
        unittest.makeSuite(CycleQueueTest),
        unittest.makeSuite(SearchArtistTest),
        unittest.makeSuite(SearchAlbumTest),
        unittest.makeSuite(SearchTrackTest),
        unittest.makeSuite(SearchAllResults),
        unittest.makeSuite(SearchArtistOneResultTest),
        unittest.makeSuite(SearchAlbumOneResultTest),
        unittest.makeSuite(SearchTrackOneResultTest),
        unittest.makeSuite(SearchNoResults),

        unittest.makeSuite(CreateTaskTest),
        unittest.makeSuite(CreateTaskSpacesTest),
        unittest.makeSuite(CreateTaskSymbolsTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
