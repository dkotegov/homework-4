# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork
from tests.createFilter import CreateFilter
from tests.config import USEREMAIL_1, USEREMAIL_2

class CreateFilterTest(unittest.TestCase):

    TEST_1_SUBJECT = 'CreateFilter. Test 1'
    TEST_2_SUBJECT = 'CreateFilter. Test 2'
    TEST_3_SUBJECT = 'CreateFilter. Test 3'

    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1920, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        self.driver.quit()

    def test_from_move_to_folder(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter('Рассылки')

        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee(USEREMAIL_1 + '@mail.ru')
        write_letter.setSubject(self.TEST_1_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_exists_and_open_it('Рассылки', self.TEST_1_SUBJECT), True)

        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()

    def test_who_delete_forever(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)
        
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee(USEREMAIL_1'@mail.ru')
        write_letter.setSubject(self.TEST_2_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_not_exists('Входящие', self.TEST_2_SUBJECT), True)

        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()

    def test_subject_cond_and_forward_to(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_forward_to(self.TEST_3_SUBJECT, USEREMAIL_2 + '@mail.ru')
        # TODO: add write letter, check and delete
    
    def test_copy_and_autoreply(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_copy_cond_and_autoreply(USEREMAIL_2)
         # TODO: add write letter, check and delete
