# -*- coding: utf-8 -*-

import unittest

from common import Page, Plate, QuestionsList, Slider, save_window
 
class ConsultantsPage(Page):
    PATH = 'all/profit/'
    PROFIT = u'По информативности'
    FRIENDLY = u'По доброжелательности'
    
    def select_rubric(self, rubric):
        self.driver.find_element_by_partial_link_text(rubric).click()
        
    def select_profit_sort(self):
        self.driver.find_element_by_partial_link_text(self.PROFIT).click()

    def select_friendly_sort(self):
        self.driver.find_element_by_partial_link_text(self.FRIENDLY).click()
                    
    def get_rubrics(self):
        return self.driver.find_elements_by_css_selector(self.RUBRIC_CLASS)
    
    def get_consultants(self):
        return self.driver.find_elements_by_css_selector('.entry_consultant')

class ConsultantsPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = ConsultPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    @save_window
    def test_select_rubric(self):
    
    @save_window
    def test_select_sort_type(self):
         
  
    @save_window
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertEqual(self.page.is_consult_form_opened(), True)
   
