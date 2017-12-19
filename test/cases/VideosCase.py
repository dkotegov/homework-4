import random
import time

from hamcrest import *

from test.cases.Case import Case
from test.ok.VideoPage import VideoPage


class VideosCase(Case):
    def setUp(self):
        super(VideosCase, self).setUp()
        self.page = VideoPage(self.driver)
        self.addPage(self.page)
        self.page.open("/video/top")

    def test1LeftMenuItemsExist(self):
        self.page.assert_left_menu_items_visible()

    def test2VideoLoadDialogOpen(self):
        self.page.assert_video_load_dialog_visible()

    def test3VideoOpen(self):
        self.page.assert_video_open()

    def test4CommentsUnderVideoExist(self):
        self.page.assert_comments_under_video_visible()

    def test5VideoInfoViewersExist(self):
        self.page.assert_video_info_viewers_visible()

    def test6VideoSuggestedExist(self):
        self.page.assert_video_suggested_exist()

    def test7VideoClosable(self):
        self.page.assert_video_is_closeable()

    def test8LiveOpen(self):
        self.page.assert_live_open()

    def test9LiveClosable(self):
        self.page.assert_live_closable()

    def test10SubscribesOpen(self):
        self.page.assert_subscribes_open()
