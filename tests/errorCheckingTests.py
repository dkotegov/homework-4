#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, ChangeFilter
from tests.config import USEREMAIL_1, USEREMAIL_2, HUB_ADDRESS, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT
from tests.createFilter import CreateFilter

class ErrorCheckingTest(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
		    command_executor = HUB_ADDRESS,
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        self.driver.quit()    

    def test_create_filter_with_empty_fields(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertEqual((error_message).encode('utf-8'), ("Не заполнены необходимые поля"))
   
    def test_create_filter_with_spaces_instead_of_text(self):
        
        create_filter = CreateFilter(self.driver)
        create_new_filter = create_filter.create_filter(condition_value = '          ', rule = Rule.field_to, change_effect = True)
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertEqual((error_message).encode('utf-8'), ("Не заполнены необходимые поля"))
    
    def test_create_dublicate_filter_test(self):
        
        for i in range(2):
            create_filter = CreateFilter(self.driver)
            create_new_filter = create_filter.create_filter(condition_value = 'test111111', rule = Rule.field_to, change_effect = True)
            create_new_filter.save_filter()

        error_message = create_new_filter.get_alert()
        #print(error_message)
        self.assertIsNotNone((error_message).encode('utf-8'))
        change_filter = ChangeFilter(self.driver)
        change_filter.delete()

    def test_filter_to_wrong_email(self):

        create_filter = CreateFilter(self.driver)
        create_new_filter = create_filter.create_filter(condition_value = 'ata-ata-ata', rule = Rule.field_to, change_effect = True, other_actions = True)
        create_new_filter.forward_to('ivan_nemshilov')
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertIsNotNone((error_message).encode('utf-8'))

    def test_filter_with_wrong_value(self):

        create_filter = CreateFilter(self.driver)
        create_new_filter = create_filter.create_filter(condition_value = 'ata-ata-ata', rule = Rule.size_KB)
        create_new_filter.delete_message()
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertIsNotNone((error_message).encode('utf-8'))

    def test_filter_with_small_value(self):

        create_filter = CreateFilter(self.driver)
        create_new_filter = create_filter.create_filter(condition_value = 'ata-ata-ata', rule = Rule.size_KB)
        create_new_filter.delete_message()
        create_new_filter.save_filter()
        error_message = create_new_filter.get_pop_up_alert()
        self.assertIsNotNone((error_message).encode('utf-8'))

    def test_filter_always_delete_all_letters(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        create_new_filter.delete_message()
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertIsNotNone((error_message).encode('utf-8'))

    def test_filter_with_auto_reply(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        create_new_filter.show_other_actions()
        create_new_filter.reply_with_mesg("            ")
        create_new_filter.save_filter()
        error_message = create_new_filter.get_alert()
        self.assertIsNotNone((error_message).encode('utf-8'))
