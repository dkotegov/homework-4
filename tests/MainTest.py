# -*- coding: utf-8 -*-
from BasicTest import BasicTest
from pages.MainPage import MainPage

import time
class LoginTest(BasicTest):
  
  def pre_tests(self):
    self.main_page = MainPage(self.driver)
    self.auth()
  
  # def test_1(self):
    