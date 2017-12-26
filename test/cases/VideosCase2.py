import random
import time

from hamcrest import *

from Case import Case
from test.ok.VideoPage import VideoPage


class VideosCase2(Case):
    def setUp(self):
        super(VideosCase2, self).setUp()
        self.page = VideoPage(self.driver)
        self.addPage(self.page)
        self.page.open("/spoemtedruzja/video")

    def test1Advertisement(self):
        self.page.assert_advertisement_visible()

    def test2LeftNav(self):
        self.page.assert_lev_nav_visible()

    def test3ContentSeparated(self):
        self.page.assert_content_vertically_separated()

    def test4VideoVisible(self):
        self.page.assert_video_is_showing()

    def test5VideoCloseable(self):
        self.page.assert_video_is_closeable()

    def test6VideoTurnable(self):
        self.page.assert_video_is_turnable()

    def test7VideoTurnableAndCloseable(self):
        self.page.assert_video_is_turnable_and_closeable()

    def test8ChanelVideos(self):
        self.page.assert_chanel_videos()

    def test9ChanelSubscription(self):
        self.page.assert_subscription_is_ok()

    def testA10ChanelSubscription(self):
        self.page.assert_klass_increase()
