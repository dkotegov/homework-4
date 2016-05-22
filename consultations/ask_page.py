# -*- coding: utf-8 -*-


import os
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities, Remote
from common import Page, QuestionsList, Slider, AskConsultantForm
       
class AskPage(Page):
    PATH = 'ask/'
    RESULT_CLASS = '.columns .column_small_10'
    
    def __init__(self, *args, **kwargs):
        super(AskPage, self).__init__(*args, **kwargs)
        self.form = AskConsultantForm(self.driver)
        
    def get_result(self):
        return self._wait_for_element(**{By.CSS_SELECTOR: self.RESULT_CLASS}).text

    
class AskPageTest(unittest.TestCase):
    TITLE = u'Мучает бессонница'
    DESCRIPTION = u'Добрый день! Уже месяц мучает бессонница по утрам.' + \
            u'Просыпаюсь в 4-5 утра и не могу заснуть больше, жутко не высыпаюсь. Подскажите, пожалуйста, как с этим бороться?'
    RUBRIC = u'Расстройства сна'
    CONSULTANT = u'Бузунов Роман Вячеславович'
    
    RESULT = u'Ваш вопрос был успешно добавлен и ожидает рассмотрения модератором'
    
    @property
    def form(self):
        return self.page.form
        
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = AskPage(self.driver)
        self.page.open()
        self.page.trigger_login()
        self.page.try_login()
        
    def tearDown(self):
        self.driver.quit()

    def test_preset_age(self):
        self.assertTrue(self.form.check_preset_age())
        
    def test_preset_gender(self):
        self.assertTrue(self.form.check_preset_gender()) 
       
    def test_submit_form(self):
        self.form.set_title(self.TITLE)
        self.form.set_description(self.DESCRIPTION)
        self.form.select_rubric(self.RUBRIC)
        self.form.select_consultant(self.CONSULTANT)
        self.form.submit()
        self.assertEqual(self.page.get_result(), self.RESULT)
        
 
if __name__ == '__main__':
    unittest.main()
       
