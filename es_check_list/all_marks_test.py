# -*- coding: utf-8 -*-

from page import *
from test import Test

ID = '575662065896'

class TestAllMarkValues(Test):

    def test(self):
        self.login(USERNAME_SECOND)

        marks = list()
        photos = list()

        expected_marks = range(1,6)

        person_page = PersonPage(self.driver, '')

        for i in expected_marks:
            photos.append(person_page.upload_photo('pic.jpg'))

        self.logout()
        self.login(USERNAME_FIRST)

        for i in expected_marks:
            photo_page = PhotoPage(self.driver, ID, photos[i - 1])
            photo_page.open()

            mark = photo_page.mark
            mark.set_mark(i)
            marks.append(int(mark.check_mark()))

        self.assertSequenceEqual(marks, expected_marks)
