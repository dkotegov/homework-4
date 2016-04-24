# -*- coding: utf-8 -*-
import os
import unittest

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
    PATH = 'list/consultant/808/'
    PROFILE_SELECTOR = '.profile-card'
    BREADCRUMBS_TITLE = u'Все консультанты - Кардиология - Здоровье Mail.Ru'
    
    def __init__(self, *args, **kwargs):
        super(OneConsultantPage, self).__init__(*args, **kwargs)
        self.element = self.driver.find_element_by_css_selector(self.PROFILE_SELECTOR)


class ConsultantsPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = OneConsultantPage(self.driver)
        self.page.open()
        
    def tearDown(self):
        self.driver.quit()

    @save_window
    def test_info(self):
        self.assertTrue(ConsultantPlate(self.page.element, self.driver).check_fields())
        
    @save_window
    def test_question_list(self):
        self.assertTrue(QuestionsList(self.driver).is_valid()) 
         
    @save_window
    def test_breadcrumbs(self):
        self.page.get_breadcrumbs().click()
        self.assertEqual(self.page.get_title(), self.page.BREADCRUMBS_TITLE)
        
    @save_window
    def test_open_consult_form(self):
        self.page.open_form()
        self.assertTrue(self.page.is_consult_form_opened())

if __name__ == '__main__':
    unittest.main()   
