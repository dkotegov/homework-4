# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from common import Page, Plate, QuestionsList, Slider

class RubricPlate(Plate):
    INNER_FIELDS = [ 
        {   #link
            'css_selector': '.list__title',
            'check_function': 'has_working_link'
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
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MainPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_slider_plate(self):
        self.assertTrue(Slider(self.driver).check_plates())

    def test_slider_nav(self):
        self.assertTrue(Slider(self.driver).check_next_slides_group())
            
    def test_rubrics(self):
        rubric = self.page.get_rubric()
        self.assertTrue(RubricPlate(rubric, self.driver).check_fields())
        
    def test_question_list_plate_fields(self):
        self.assertTrue(QuestionsList(self.driver).check_plates())       

    def test_question_list_nav(self):
        question_list = QuestionsList(self.driver)
        question_list.go_to_next_page()
        self.assertTrue(question_list.check_plates())
          
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())
        
if __name__ == '__main__':
    unittest.main()   
