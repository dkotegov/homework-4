# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter, Step

class CreateFilter(Step):

    def create_filter(self, condition_value, rule = None, change_effect = False, other_actions = False):
        new_filter = CreateNewFilter(self.driver)
        new_filter.open()
        condition_index = 0
        if rule != None:
            new_filter.change_condition(rule, condition_index)
        new_filter.change_condition_value(condition_index, condition_value)
        if change_effect:
            new_filter.change_condition_effect(condition_index)
        if other_actions:
            new_filter.show_other_actions()
            self.driver.execute_script("window.scrollTo(0, 200)") 
        return new_filter

    def create_to_cond_and_move_to_folter(self, folderName):
        '''
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        '''
        create_new_filter = self.create_filter('it-berries')
        create_new_filter.move_to_folder(folderName)
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    def create_subject_cond_and_delete(self, subject):
        '''
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_subject, condition_index)
        create_new_filter.change_condition_value(condition_index, subject)
        '''
        create_new_filter = self.create_filter(condition_value = subject, rule = Rule.field_subject)
        create_new_filter.delete_message()
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    def create_subject_cond_and_forward_to(self, subject, email):
        '''
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_subject, condition_index)
        create_new_filter.change_condition_value(condition_index, subject)
        create_new_filter.show_other_actions()
        '''
        create_new_filter = self.create_filter(condition_value = subject, rule = Rule.field_subject, other_actions = True)
        create_new_filter.forward_to(email)
        create_new_filter.save_filter()
        try:
            create_new_filter.confirm_password() # Need to confirm "forward to" operation with password (not all the time??)
        except:
            print("Password confirmation exception!") # little trick to confirm password
        create_new_filter.check_if_filter_list_exists()

    def create_copy_cond_and_autoreply(self, copyValue):
        '''
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_copy, condition_index)
        create_new_filter.change_condition_value(condition_index, copyValue)
        create_new_filter.change_condition_effect(condition_index)
        create_new_filter.show_other_actions()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        '''
        create_new_filter = self.create_filter(condition_value = copyValue, rule = Rule.field_copy, other_actions = True)
        create_new_filter.reply_not_found()
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    def create_subject_cond_and_flag(self, subject):
        '''
        create_filter = CreateNewFilter(self.driver)
        create_filter.open()
        condition_index = 0
        create_filter.change_condition(Rule.field_subject, condition_index)
        create_filter.change_condition_value(condition_index, subject)
        '''
        create_new_filter = self.create_filter(condition_value = subject, rule = Rule.field_subject, other_actions = True)
        create_new_filter.action_flag()
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    def create_redirect_from_cond_and_continue(self, email):
        '''
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_redirected_from, condition_index)
        create_new_filter.change_condition_value(condition_index, email)
        create_new_filter.show_other_actions()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        '''
        create_new_filter = self.create_filter(condition_value = email, rule = Rule.field_redirected_from, other_actions = True)
        create_new_filter.continue_to_filter()
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    #TODO: check where to place this??? 
    def delete_created_filter(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.delete_all()
