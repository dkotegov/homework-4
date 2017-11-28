# -*- coding: utf-8 -*-

from base import BaseTest
from tests.pages.discussions.pages import DiscPage

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
