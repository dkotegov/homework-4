# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, Plate, QuestionsList, Slider, save_window

from selenium import webdriver #TODO: remove

class RubricPlate(Plate):
    INNER_FIELDS = [ 
        {   #link
            'css_selector': '.list__title',
            'check_function': 'has_link_with_title'
        },
        {   #title
            'css_selector': '.list__title',
            'check_function': 'has_text'
        }                
    ]
        
class MainPage(Page):
    RUBRIC_CLASS = '.list_rubric'
    
    def get_rubric(self):
        return self.driver.find_element_by_css_selector(self.RUBRIC_CLASS)


class MainPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        #self.driver = Remote(
        #    command_executor='http://127.0.0.1:4444/wd/hub',
        #    desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        #)
        self.driver = webdriver.Firefox()
        self.page = MainPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_slider(self):
        self.assertTrue(Slider(self.driver).is_valid())
    
    def _test_rubrics(self):
        rubric = self.page.get_rubric()
        self.assertTrue(RubricPlate(rubric, self.driver).check_fields())
        
    def _test_question_list(self):
        self.assertTrue(QuestionsList(self.driver).is_valid())       
  
    @save_window
    def _test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())
        
if __name__ == '__main__':
    unittest.main()   
