# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter, Step

class CreateFilter(Step):

    def create_to_cond_and_move_to_folter(self, folderName):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        create_new_filter.move_to_folder(folderName)
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    def create_subject_cond_and_delete(self, subject):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_subject, condition_index)
        create_new_filter.change_condition_value(condition_index, subject)
        create_new_filter.delete_message()
        create_new_filter.save_filter()
        create_new_filter.check_if_filter_list_exists()

    #TODO: check where to place this??? 
    def delete_created_filter(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.delete()
