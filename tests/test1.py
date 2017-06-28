# -*- coding: utf-8 -*-

import re

from event_list import EventListTest

class Test1(EventListTest):
    '''Check if header redirects to event page'''

    def test(self):
        super(Test1, self).test()
        event = self.event_list_page.event
        event.open_event()
        is_url_correct = re.match(r'^http://ftest\.tech-mail\.ru/blog/topic/view/[0-9]+/$',
                                  self.driver.current_url) is not None
        self.assertTrue(is_url_correct)
