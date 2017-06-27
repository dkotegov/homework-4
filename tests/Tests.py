# -*- coding: utf-8 -*-
import os

import unittest
from PageObjects import *

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

class MyTest(unittest.TestCase):
   USEREMAIL = 'dvpitakov@gmail.com.local'
   PASSWORD = os.environ['PASSWORD']
   USERNAME = u'Дмитрий Питаков'

   def setUp(self):
      browser = os.environ.get('BROWSER', 'CHROME')

      self.driver = Remote(
         command_executor = 'http://127.0.0.1:4444/wd/hub',
         desired_capabilities = DesiredCapabilities.CHROME
      )

   def tearDown(self):
      self.driver.quit()

   def test_first(self):
      auth_page = AuthPage(self.driver)
      auth_page.open()

      auth_form = auth_page.form
      auth_form.open_form()
      auth_form.set_login(self.USEREMAIL)
      auth_form.set_password(self.PASSWORD)
      auth_form.submit()
      user_name = auth_page.top_menu.get_username()
      self.assertEqual(self.USERNAME, user_name)
