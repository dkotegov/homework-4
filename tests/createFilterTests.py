# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, Cleaner
from support.folders import Folder
from tests.createFilter import CreateFilter
from tests.config import USEREMAIL_1, USEREMAIL_2, HUB_ADDRESS, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT

class CreateFilterTest(unittest.TestCase):

    TEST_1_SUBJECT = 'CreateFilter. Test 1'
    TEST_2_SUBJECT = 'CreateFilter. Test 2'
    TEST_3_SUBJECT = 'CreateFilter. Test 3'
    TEST_4_SUBJECT = 'CreateFilter. Test 4'
    TEST_5_SUBJECT = 'CreateFilter. Test 5'
    
    current_test = 'ERROR'

    def setUp(self):
        #open filter settings

        self.driver = Remote(
		    command_executor = HUB_ADDRESS,
	        desired_capabilities = DesiredCapabilities.CHROME )
        self.driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        #delete all messages and created filters

        create_filter = CreateFilter(self.driver)
        cleaner = Cleaner(self.driver)
        check_filter_work = CheckFilterWork(self.driver)
        cleaner.delete_all_letters()
        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()
        self.driver.quit()

    def test_from_move_to_folder(self):
        #create a filter that moves the message

        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter(Folder.NEWSLETTERS)

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_1_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.NEWSLETTERS, self.TEST_1_SUBJECT))

    def test_who_delete_forever(self):
        #create a filter that deletes messages

        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)
        
        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_2_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_not_exists(Folder.INBOX, self.TEST_2_SUBJECT))

    def test_subject_cond_and_forward_to(self):
        #create a filter that deletes messages

        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_forward_to(self.TEST_3_SUBJECT, USEREMAIL_2 + '@mail.ru')

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_3_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.SENT, self.TEST_3_SUBJECT))

    def test_copy_and_autoreply(self):
        #create a filter that deletes messages

        create_filter = CreateFilter(self.driver)
        create_filter.create_copy_cond_and_autoreply(USEREMAIL_2)

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_4_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.SENT, self.TEST_4_SUBJECT))

    def test_redirect_from_and_continue_to_filter(self):
        #create a filter that redirects and enables the following filter

        create_filter = CreateFilter(self.driver)

        create_new_filter = create_filter.create_filter(condition_value = USEREMAIL_1 + '@mail.ru', rule = Rule.field_redirected_from, change_effect = True, other_actions = True)
        create_new_filter.continue_to_filter()
        create_new_filter.save_filter()

        create_filter.create_subject_cond_and_flag(self.TEST_5_SUBJECT)

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_5_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.SENT, self.TEST_5_SUBJECT))