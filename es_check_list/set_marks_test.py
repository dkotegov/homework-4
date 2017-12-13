# -*- coding: utf-8 -*-

from page import USERNAME_FIRST, USERNAME_SECOND, PhotoPage
from BasicTest import BasicTest

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class AllMarkValuesTest(BasicTest):

    def test(self):
        marks = range(1, 6)

        photos = self.upload_photo(USERNAME_SECOND, len(marks))
        self.photos = photos
        name = self.get_name(USERNAME_FIRST)
        self.set_marks(None, photos, marks)
        self.assertTrue(self.check_marks(USERNAME_SECOND, photos, marks, name, False))


class SelfMarkTest(BasicTest):
    def test(self):
        marks = [5]
        photos = self.upload_photo(USERNAME_SECOND, len(marks), False)
        self.photos = photos
        self.assertFalse(self.set_marks(None, photos, marks, False))


class UpdateMarkTest(BasicTest):
    def test(self):
        marks = [5]

        photos = self.upload_photo(USERNAME_SECOND, len(marks))
        self.photos = photos
        self.set_marks(USERNAME_FIRST, photos, marks, False)

        photo_page = PhotoPage(self.driver, photos[0][1], photos[0][0])
        photo_page.open()
        mark = photo_page.mark

        self.assertTrue(mark.update())
