# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, QuestionsList, Slider, save_window
        
class QuestionPage(Page):
    PATH = '1909637/'
    CONSULTANT_LINK = '.entry__info-name .entry__info-link'
    VOTE_FORM_SELECTOR = '.js-form_vote__item'
    VOTE_SCORE_SELECTOR = '.stars__item'
    VOTE_USER_SCORE = '.stars__label'
    
    def get_consultant_link(self):
       return self.driver.find_element_by_css_selector(self.CONSULTANT_LINK)
      
    def _get_vote_div(self, vote_type):
       for el in self.driver.find_elements_by_css_selector(self.VOTE_FORM_SELECTOR):
           if el.get_attribute('data-type') == vote_type: return el
    
    def vote(self, vote_type, score):
       el = self._get_vote_div(self, vote_type)  
       for i, score_el in enumerate(el.find_elements_by_css_selector(self.VOTE_SCORE_SELECTOR)):
           if i == int(score_el.get_attribute('data-value')) - 1: 
               score_el.click()
               
    def get_user_score(self, vote_type):
        self._wait_for_element(**{By.CLASS_NAME: self.VOTE_USER_SCORE}) 
        el = self._get_vote_div(self, vote_type)
        for score_el in el.find_elements_by_css_selector(self.VOTE_USER_SCORE):
            if score_el.is_displayed(): return score_el.text
            
class QuestionPageTest(unittest.TestCase):
    
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

    @save_window
    def test_breadcrumbs(self):
        text = self.page.get_breadcrumbs().text
        self.page.get_breadcrumbs().click()
        self.assertGreater(self.page.get_title().find(), -1)
                
    @save_window
    def test_consultant_link(self):
        text = self.page.get_consultant_link.text
        self.page.get_consultant_link.click()
        self.assertGreater(self.page.get_title().find(), -1)
    
    def test_profit_score(self):
        score = 4
        self.vote('profit', score)
        res_score = self.get_user_score('profit')
        self.assertEqual(int(res_score.split('/')[0]), score(
        
    @save_window
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())
        
if __name__ == '__main__':
    unittest.main()     
