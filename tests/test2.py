# -*- coding: utf-8 -*-

from event_list import EventListTest

class Test2(EventListTest):
    '''Check if registration button doesn't change its text on click when registration is closed'''

    def test(self):
        super(Test2, self).test()
        event = self.event_list_page.event
        old_text = event.get_button_text()
        event.participate()
        new_text = event.get_button_text()
        self.assertEqual(old_text, new_text, 'Текст кнопки регистрация изменился!')
