# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, Plate, QuestionsList, Slider
 
class ConsultantsPage(Page):
    PATH = 'all/profit/'
    CONSULTANT_SELECTOR = '.entry_consultant'
    TAB_TEXT_SELECTOR = '.tabs__item_active .link__text'
    PROFIT = u'По информативности'
    FRIENDLY = u'По доброжелательности'
    
    def select_rubric(self, rubric):
        self.driver.find_element_by_partial_link_text(rubric).click()
        
    def select_profit_sort(self):
        self.driver.find_element_by_partial_link_text(self.PROFIT).click()

    def select_friendly_sort(self):
        self.driver.find_element_by_partial_link_text(self.FRIENDLY).click()     
    
    def get_consultants(self):
        return self.driver.find_elements_by_css_selector(self.CONSULTANT_SELECTOR)
     
    def get_current_tab_text(self):
        return self.driver.find_element_by_css_selector(self.TAB_TEXT_SELECTOR).text

class ConsultantsPageTest(unittest.TestCase):
    RUBRIC = u'Кардиология'
    RUBRIC_URL = 'cardiology'
    
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = ConsultantsPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    def test_select_rubric(self):
        self.page.select_rubric(self.RUBRIC)
        self.assertGreater(self.driver.current_url.find(self.RUBRIC_URL), -1)
        
    def test_select_sort_type(self):      
        self.page.select_friendly_sort()
        self.assertEqual(self.page.get_current_tab_text(), self.page.FRIENDLY)
        
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())

if __name__ == '__main__':
    unittest.main()   
