# -*- coding: utf-8 -*-

from page import *
from test import Test


class TestAllMarkValues(Test):

    def test(self):
        self.login()

        marks = list()

        expected_marks = range(1,6)

        for i in expected_marks:
            online_page = OnlinePage(self.driver)
            online_page.open()
            person_page = online_page.first_person()
            avatar = person_page.avatar
            avatar.open()

            mark = Mark(self.driver)
            mark.set_mark(i)
            marks.append(int(mark.check_mark()))

        self.assertSequenceEqual(marks, expected_marks)
