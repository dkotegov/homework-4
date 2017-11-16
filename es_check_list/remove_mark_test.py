# -*- coding: utf-8 -*-

import time

from page import *
from test import Test


class TestRemoveMark(Test):

    def test(self):
        mark_value = 5

        self.login(USERNAME_SECOND)

        person_page = PersonPage(self.driver, '')
        photo = person_page.photo_manager.upload_photo('pic.jpg')

        self.logout()
        self.login(USERNAME_FIRST)

        person_page = PersonPage(self.driver, '')

        name = person_page.get_name()

        photo_page = PhotoPage(self.driver, photo[1], photo[0])
        photo_page.open()

        mark = photo_page.mark
        mark.set_mark(mark_value)

        self.logout()

        self.login(USERNAME_SECOND)

        person_page = PersonPage(self.driver, '')

        photo_page = PhotoPage(self.driver, photo[1], photo[0])
        photo_page.open()

        marks = photo_page.marks
        marks.open()

        marks.remove(name)

        photo_page.open()

        marks = photo_page.marks
        marks.open()

        result = marks.check_mark(mark_value, name)
        self.assertFalse(result)
