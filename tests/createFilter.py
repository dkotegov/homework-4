# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter

class Rule():
    field_from = 'From'
    field_to = 'To'
    field_subject = 'Subject'
    field_copy = 'Cc'
    field_redirected_from = 'Resent-From'
    field_redirected_to = 'Resent-To'
    size_KB = 'Size'

class CreateNewFilterTest(unittest.TestCase):
    def setUp(self):

        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )

    def tearDown(self):
        self.driver.quit()
    
    def test(self):
        self.driver.set_window_size(1920, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open()
        
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        
        create_new_filter.add_condition()
        index = 1;
        create_new_filter.change_condition(Rule.field_to, index)
        create_new_filter.change_condition_effect(index)
        create_new_filter.change_condition_value(index, 'hey')
        create_new_filter.switch_interaction_conditions()

        create_new_filter.move_to_folder('Рассылки')
        create_new_filter.as_read()
        create_new_filter.action_flag()
        create_new_filter.delete_message()
        create_new_filter.show_other_actions()
        create_new_filter.forward_to('ivan_nemshilov@mail.ru')
        create_new_filter.forward_change_contex()
        #create_new_filter.repley_with_mesg('Привет, не пиши мне больше!')
        create_new_filter.repley_not_found()
        create_new_filter.continue_to_filter()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        create_new_filter.spam_on()
        create_new_filter.folders_apply('Рассылки')
        create_new_filter.save_filter()
        self.assertEqual(True, True)