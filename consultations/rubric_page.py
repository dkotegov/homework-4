# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, QuestionsList, Slider, Plate

class QuestionPlateRubric(Plate):
    INNER_FIELDS = [ 
        {   #title
            'css_selector': 'div.entry__name a.entry__link',
            'check_function': 'has_link_with_title'
        },
        {   #descrption
            'css_selector': '.entry__description',
            'check_function': 'has_text'
        }                
    ]
            
class RubricPage(Page):
    PATH = 'list/rubric/cardiology/'
    
class RubricPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver = webdriver.Firefox()
        self.page = RubricPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_slider_plate_fields(self):
        self.assertTrue(Slider(self.driver).check_plates())

    def test_slider_nav(self):
        self.assertTrue(Slider(self.driver).check_next_slides_group())
  
    def test_question_list_plate_fields(self):
        self.assertTrue(QuestionsList(self.driver, plate_class=QuestionPlateRubric).check_plates())       

    def test_question_list_nav(self):
        question_list = QuestionsList(self.driver, plate_class=QuestionPlateRubric)
        question_list.go_to_next_page()
        self.assertTrue(question_list.check_plates()) 
         
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())

if __name__ == '__main__':
    unittest.main()
