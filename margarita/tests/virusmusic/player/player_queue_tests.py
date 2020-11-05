from margarita.tests.virusmusic.player.default import Test
from margarita.pages.virusmusic.main_page import MainPage


class TrackPlayTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        player_pos_before = page.get_player_pos()
        page.play(track_id)
        player_pos_after = page.get_player_pos()
        self.assertNotEqual(player_pos_after, player_pos_before)


class TrackRemoveFromQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        self.assertTrue(page.queue_contains(track_id))
        page.remove_from_queue(track_id)
        self.assertFalse(page.queue_contains(track_id))


class TrackPlayFromQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        current_before = page.get_current_id()
        page.play_track_in_queue(3)
        current_after = page.get_current_id()
        self.assertNotEqual(current_before, current_after)


class TrackNextQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        current_before = page.get_current_id()
        page.play_next()
        current_after = page.get_current_id()
        self.assertNotEqual(current_before, current_after)


class TrackPrevQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        page.play_track_in_queue(3)
        current_before = page.get_current_id()
        page.play_prev()
        current_after = page.get_current_id()
        self.assertNotEqual(current_before, current_after)

class ShuffleQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        page.play_next()
        next_track_before = page.get_current_id()
        page.play_prev()
        page.shuffle()
        next_track_after = page.play_next()
        self.assertNotEqual(next_track_before, next_track_after)

class CycleQueueTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.open()
        track_id = page.get_first_track_id()
        page.play(track_id)
        page.cycle()
        page.play_track_in_queue(9)
        page.play_next()
        cur_id = page.get_current_id()
        self.assertEqual(cur_id, track_id)