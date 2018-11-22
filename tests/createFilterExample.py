# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, LogOut
from tests.config import USEREMAIL_1, USEREMAIL_2

class CreateFilterExample(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1920, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        self.driver.quit()
    '''
    def test_create_filter(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()

        index = 0;
        create_new_filter.change_condition(Rule.field_to, index)
        create_new_filter.change_condition_effect(index)
        create_new_filter.change_condition_value(index, 'hey')

        create_new_filter.move_to_folder('Рассылки')
        create_new_filter.as_read()
        create_new_filter.action_flag()
        create_new_filter.delete_message()
        create_new_filter.show_other_actions()
        create_new_filter.forward_to('ivan_nemshilov@mail.ru')
        create_new_filter.forward_change_contex()
        #create_new_filter.reply_with_mesg('Привет, не пиши мне больше!')
        create_new_filter.reply_not_found()
        create_new_filter.continue_to_filter()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        create_new_filter.spam_on()
        create_new_filter.folders_apply('Рассылки')
        create_new_filter.save_filter()
        self.assertEqual(True, True)

    def test_create_another_filter(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()

        index = 0;
        create_new_filter.change_condition(Rule.field_to, index)
        create_new_filter.change_condition_effect(index)
        create_new_filter.change_condition_value(index, 'hey')
        
        create_new_filter.add_condition()
        index = 1;
        create_new_filter.change_condition_value(index, "what's up?")
        
        create_new_filter.switch_interaction_conditions()

        create_new_filter.move_to_folder('Рассылки')
        create_new_filter.as_read()
        create_new_filter.action_flag()
        create_new_filter.delete_message()
        create_new_filter.show_other_actions()
        create_new_filter.forward_to('ivan_nemshilov@mail.ru')
        create_new_filter.reply_with_mesg('Привет, не пиши мне больше!')
        create_new_filter.reply_not_found()
        create_new_filter.continue_to_filter()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        create_new_filter.spam_on()
        create_new_filter.folders_apply('Рассылки')
        create_new_filter.save_filter()
        self.assertEqual(True, True)
    '''
    def test_logut(self):
        log_out = LogOut(self.driver)
        log_out.log_out()