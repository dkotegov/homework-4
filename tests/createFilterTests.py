# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork
from tests.createFilter import CreateFilter

class CreateFilterTest(unittest.TestCase):

    TEST_2_SUBJECT = 'CreateFilter. Test 2'

    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1920, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open()

    def tearDown(self):
        self.driver.quit()

    def test_from_move_to_folder(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter('Рассылки')

        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject('Технопарк')
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_exists_and_open_it('Рассылки', 'Технопарк'), True)

        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()

    def test_who_delete_forever(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)
        
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject(self.TEST_2_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_not_exists('Рассылки', self.TEST_2_SUBJECT), True)

        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()
