# -*- coding: utf-8 -*-

import time

from page import *
from BasicTest import BasicTest


class TestRemoveMark(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.remove_marks(USERNAME_SECOND, photos, name, False)

        self.assertFalse(self.check_marks(None, photos, marks, name, False))


class CancelRemoveMarkTest(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.remove_marks(USERNAME_SECOND, photos, name, False, True)

        self.assertTrue(self.check_marks(None, photos, marks, name, False))


class TestSetNewMark(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.remove_marks(USERNAME_SECOND, photos, name)

        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.assertTrue(self.check_marks(USERNAME_SECOND, photos, marks, name, False))

