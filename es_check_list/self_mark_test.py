# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page import *

from test import Test


class TestSelfMark(Test):
    def test(self):
        self.login(USERNAME_FIRST)

        person_page = PersonPage(self.driver, '')

        avatar = person_page.avatar
        avatar.open()

        mark = Mark(self.driver)
        mark_value = mark.set_mark()

        self.assertEqual(mark_value, 0)



