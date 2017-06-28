# -*- coding: utf-8 -*-

import re

from event_list import EventListTest, EventListPage

class Test4(EventListTest):
    '''Check if subheader redirects to event list'''

    def test(self):
        super(Test4, self).test()
        event = self.event_list_page.event
        event.open_blog()
        print self.driver.current_url
        print EventListPage.get_url()
        is_url_correct = self.driver.current_url == EventListPage.get_url()
        self.assertTrue(is_url_correct)
