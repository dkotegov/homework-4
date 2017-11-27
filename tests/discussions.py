# -*- coding: utf-8 -*-

from base import BaseTest
from tests.pages.discussions.discussions import DiscussionsPage


class DiscussionsTest(BaseTest):

    def test_discussions_open(self):
        discussions_page = DiscussionsPage(self.driver)
        discussions_page.navigate()
        self.assertTrue(discussions_page.is_opened(), 'discussions opened')


