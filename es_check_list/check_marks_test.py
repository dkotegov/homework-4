# -*- coding: utf-8 -*-

import time

from page import *
from test import Test


class TestCheckMarks(Test):

    def test(self):
        self.login()

        person_page = PersonPage(self.driver, '')

        avatar = person_page.avatar
        avatar.open()
        person_page.open_counter()

        marks_modal = avatar.marks
        result = marks_modal.check_mark(2, "Артур Селезнёв")

        #time.sleep(5)
        self.assertTrue(result)
