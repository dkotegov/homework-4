# -*- coding: utf-8 -*-

from event_list import EventListTest

class Test3(EventListTest):
    '''Check if registration button doesn't change its color on click when registration is closed'''

    def test(self):
        super(Test3, self).test()
        event = self.event_list_page.event
        old_color = event.get_button_color()
        event.participate()
        new_color = event.get_button_color()
        self.assertEqual(old_color, new_color, 'Текст кнопки регистрация изменился!')
