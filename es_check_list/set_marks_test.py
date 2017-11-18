# -*- coding: utf-8 -*-

from page import *
from BasicTest import BasicTest

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TestAllMarkValues(BasicTest):

    def test(self):
        marks = range(1,6)

        photos = self.upload_photo(USERNAME_SECOND, len(marks))
        name = self.set_marks(USERNAME_FIRST, photos, marks)

        self.assertTrue(self.check_marks(USERNAME_SECOND, photos, marks, name, False))


class TestSelfMark(BasicTest):
    def test(self):
        self.login(USERNAME_FIRST)

        person_page = PersonPage(self.driver, '')

        avatar = person_page.avatar
        avatar.open()

        mark = Mark(self.driver)
        mark_value = mark.set_mark()

        self.assertEqual(mark_value, 0)