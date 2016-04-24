# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, QuestionsList, Slider, save_window

        
class RubricPage(Page):
    PATH = 'list/rubric/cardiology/'
    
class RubricPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = RubricPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_slider(self):
        self.assertTrue(Slider(self.driver).is_valid())
        
    def test_question_list(self):
        self.assertTrue(QuestionsList(self.driver).is_valid())       
  
    @save_window
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())

if __name__ == '__main__':
    unittest.main()
