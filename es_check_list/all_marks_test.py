# -*- coding: utf-8 -*-

from page import *
from test import Test


class TestAllMarkValues(Test):
    def test(self):
        marks = list()

        expected_marks = range(1,6)
        self.photos = self.upload_photo(USERNAME_SECOND, len(expected_marks))
        self.login(USERNAME_FIRST)

        ID = self.photos[0][1]

        for i in expected_marks:
            photo_page = PhotoPage(self.driver, ID, self.photos[i - 1][0])
            photo_page.open()

            mark = photo_page.mark
            mark.set_marks(i)
            marks.append(int(mark.check_mark()))

        self.remove_photos(USERNAME_SECOND, self.photos)

        self.assertSequenceEqual(marks, expected_marks)
