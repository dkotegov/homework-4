# -*- coding: utf-8 -*-
import random
import string

from base import BaseTest
from tests.pages.discussions.pages import DiscPage
from tests.pages.discussions.discussions import DiscussionsPage
from tests.pages.main import MainPage

from tests.pages.posts import PostsPage


class DiscussionsTest(BaseTest):
    def setUp(self):
        super(DiscussionsTest, self).setUp()
        drv = self.driver
        self.page = DiscPage(drv)

    def test_visible_user_card(self):
        self.page.check_visible_user_info()
        pass

    def test_visible_button_card(self):
        self.page.downbutton_showed()
        pass

    def test_visible_classlist(self):
        self.page.class_showed()
        pass

    def test_visible_warn(self):
        self.page.warn_showed()
        pass

    def test_visible_time(self):
        self.page.time_showed()
        pass

    def test_discussions_open(self):
        discussions_page = DiscussionsPage(self.driver)
        discussions_page.navigate()
        self.assertTrue(discussions_page.is_opened(), 'discussions not opened')

    def test_tab_participated_open(self):
        dp = DiscussionsPage(self.driver)
        dp.navigate()
        elm1 = dp.openParticipatedTab()
        elm2 = dp.selectedTab()
        self.assertEquals(elm1,elm2,"Participated not opened")

    def test_tab_my_posts_open(self):
        dp = DiscussionsPage(self.driver)
        dp.navigate()
        elm1 = dp.openMyPostsTab()
        elm2 = dp.selectedTab()
        self.assertEquals(elm1,elm2,"My posts not opened")

    def test_tab_friends_open(self):
       dp = DiscussionsPage(self.driver)
       dp.navigate()
       elm1 = dp.openFriendsTab()
       elm2 = dp.selectedTab()
       self.assertEquals(elm1,elm2,"Friends not opened")

    def test_tab_groups_open(self):
        dp = DiscussionsPage(self.driver)
        dp.navigate()
        elm1 = dp.openGrupsTab()
        elm2 = dp.selectedTab()
        self.assertEquals(elm1, elm2,"Groups not opened")

    def test_create_my_publish(self):
        text = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        postPage = PostsPage(self.driver)
        postPage.navigate()
        postPage.create_my_discussions(text)
        DiscussionsPage.setComment(self,"first comment")
        text2 = DiscussionsPage.getCurrentDiscussionTitle(self)
        self.assertEquals(unicode(text,"utf-8"),text2,"my publish not created")

    def test_create_comment_for_my_publish(self):
        text_discussion_title = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        text_comment = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        postPage = PostsPage(self.driver)
        postPage.navigate()
        postPage.create_my_discussions(text_discussion_title)
        DiscussionsPage.setComment(self, text_comment)

        text2 = DiscussionsPage.getLastCommentInCurrentDiscussion(self)
        self.assertEquals(unicode(text_comment, "utf-8"), text2, "my comment not created")