# -*- coding: utf-8 -*-

import time

from page import *
from test import Test


class TestSetNewMark(Test):

    def test(self):
        mark_value = 5
        marks = [mark_value]

        photos = self.upload_photo(USERNAME_SECOND)
        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.remove_marks(USERNAME_SECOND, photos, name)

        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.assertTrue(self.check_marks(USERNAME_SECOND, photos, marks, name, False))
