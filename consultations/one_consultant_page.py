# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities, Remote

from common import Page, Plate, QuestionsList, save_window
 
class ConsultantPlate(Plate):
    INNER_FIELDS = [ 
        {   #image
            'css_selector': '.image__img',
            'check_function': 'has_image'
        },
        {   #rating
            'css_selector': '.rating__cell .rating__value .link__text',
            'check_function': 'has_text'
        },
        {   #descrption
            'css_selector': '.article__item_html',
            'check_function': 'has_text'
        }                
    ]
    
class OneConsultantPage(Page):
    PATH = 'list/consultant/449/'
    PROFILE_SELECTOR = '.profile-card'
    BREADCRUMBS_TITLE = u'Специалисты'
    
    def __init__(self, *args, **kwargs):
        super(OneConsultantPage, self).__init__(*args, **kwargs)
        
    def set_element(self):
        self.element = self._wait_for_element(**{By.CSS_SELECTOR: self.PROFILE_SELECTOR})


class OneConsultantPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = OneConsultantPage(self.driver)
        self.page.open()
        self.page.set_element()
        
    def tearDown(self):
        self.driver.quit()

    def _test_info(self):
        self.assertTrue(ConsultantPlate(self.page.element, self.driver).check_fields())
        
    def _test_question_list(self):
        self.assertTrue(QuestionsList(self.driver).is_valid()) 
         
    def _test_breadcrumbs(self):
        self.page.get_breadcrumbs().click()
        self.assertEqual(self.page.get_title(), self.page.BREADCRUMBS_TITLE)
        
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())

if __name__ == '__main__':
    unittest.main()   
