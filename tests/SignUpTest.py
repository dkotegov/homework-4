# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.SignUpPage import SignUpPage
from pages.MainPage import MainPage

import time

class SignUpTest(BasicTest):
  
  def setUp(self):
    super(SignUpTest, self).setUp()
    self.signup_page = SignUpPage(self.driver)
    self.signup_page.open()
    
  def test_correct_registration(self):
    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": 4,
      "year": 2010,
      "sex": True,
      "email": self.signup_page.generate_fake_email(),
      "domain": False,
      "password": self.signup_page.generate_fake_password(),
      "addition_email": False
    }
    self.signup_page.signup(data)
    self.signup_page.wait_redirect(self.MAIL_URL)
    