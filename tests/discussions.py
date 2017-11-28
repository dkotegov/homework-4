# -*- coding: utf-8 -*-

from base import BaseTest
from tests.pages.discussions.discussions import DiscussionsPage
from tests.pages.main import MainPage

from tests.pages.posts import PostsPage


class DiscussionsTest(BaseTest):

    # def test_discussions_open(self):
    #     discussions_page = DiscussionsPage(self.driver)
    #     discussions_page.navigate()
    #     self.assertTrue(discussions_page.is_opened(), 'discussions not opened')
    #
    # def test_tab_participated_open(self):
    #     dp = DiscussionsPage(self.driver)
    #     dp.navigate()
    #     elm1 = dp.openParticipatedTab()
    #     elm2 = dp.selectedTab()
    #     self.assertEquals(elm1,elm2,"Participated not opened")
    #
    # def test_tab_my_posts_open(self):
    #     dp = DiscussionsPage(self.driver)
    #     dp.navigate()
    #     elm1 = dp.openMyPostsTab()
    #     elm2 = dp.selectedTab()
    #     self.assertEquals(elm1,elm2,"My posts not opened")
    #
    # def test_tab_friends_open(self):
    #    dp = DiscussionsPage(self.driver)
    #    dp.navigate()
    #    elm1 = dp.openFriendsTab()
    #    elm2 = dp.selectedTab()
    #    self.assertEquals(elm1,elm2,"Friends not opened")
    #
    # def test_tab_groups_open(self):
    #     dp = DiscussionsPage(self.driver)
    #     dp.navigate()
    #     elm1 = dp.openGrupsTab()
    #     elm2 = dp.selectedTab()
    #     self.assertEquals(elm1, elm2,"Groups not opened")

    def test_create_my_publish(self):
        text = "ПАСАНЫ Я СОЗДАЛ 3"
        postPage = PostsPage(self.driver)
        postPage.navigate()
        postPage.create_my_discussions(text)
        DiscussionsPage.setComment(self,"first comment")
        self.assertEquals(unicode(text,"utf-8"),DiscussionsPage.getCurrentDiscussionTitle(self),"my publish not created")