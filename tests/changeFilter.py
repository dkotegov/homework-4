# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter

class ChangeFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1920, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open()

    def tearDown(self):
        self.driver.quit()

    def test_change(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0;
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        create_new_filter.move_to_folder('Рассылки')
        create_new_filter.save_filter()

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.move_to_folder('Социальные сети')
        change_filter.save_filter()
        change_filter.delete()
    #TODO: create tests functions