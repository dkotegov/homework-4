# -*- coding: utf-8 -*-

from page import *
from BasicTest import BasicTest


class RemoveMarkTest(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        self.photos = photos
        name = self.get_name(USERNAME_FIRST)
        self.set_marks(None, photos, marks)

        if self.remove_marks(USERNAME_SECOND, photos, name, False):
            result = not self.check_marks(None, photos, marks, name, False)
        else:
            result = None

        self.assertTrue(result)


class CancelRemoveMarkTest(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        self.photos = photos
        name = self.get_name(USERNAME_FIRST)
        self.set_marks(None, photos, marks)

        if self.remove_marks(USERNAME_SECOND, photos, name, False, True):
            result = self.check_marks(None, photos, marks, name, False)
        else:
            result = None

        self.assertTrue(result)


class SetNewMarkTest(BasicTest):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        self.photos = photos
        name = self.get_name(USERNAME_FIRST)
        self.set_marks(None, photos, marks)

        if self.remove_marks(USERNAME_SECOND, photos, name):
            name = self.get_name(USERNAME_FIRST)
            self.set_marks(None, photos, marks)
            result = self.check_marks(USERNAME_SECOND, photos, marks, name, False)
        else:
            result = None

        self.assertTrue(result)
