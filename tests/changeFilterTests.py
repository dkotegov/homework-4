# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter, LogOut, Cleaner
from support.folders import Folder
from tests.createFilter import CreateFilter
from tests.config import USEREMAIL_1, USEREMAIL_2, HUB_ADDRESS, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT

class ChangeFilterTest(unittest.TestCase):

    TEST_1_SUBJECT = 'Test 1 - Change MoveTo to Delete'
    TEST_2_SUBJECT = 'Test 2 - Change Delete to MoveTo'
    TEST_3_SUBJECT = 'Test 3 - Add cond Size and SendNotification'
    TEST_4_SUBJECT = 'Test 4 - Add cond Copy and revert AutoReply'
    TEST_5_SUBJECT = 'Test 5 - Redirected to'

    def setUp(self):
        self.driver = Remote(
		    command_executor = HUB_ADDRESS,
	        desired_capabilities = DesiredCapabilities.CHROME )
        self.driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        create_filter = CreateFilter(self.driver)
        cleaner = Cleaner(self.driver)
        check_filter_work = CheckFilterWork(self.driver)
        cleaner.delete_all_letters()
        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()
        self.driver.quit()
    
    # TODO: camel case style?
    def test_change_move_to_delete(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter(Folder.NEWSLETTERS)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.delete_message()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_1_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_not_exists(Folder.NEWSLETTERS, self.TEST_1_SUBJECT))
        #check_filter_work.open_filters_page_in_new_window()
        #change_filter.delete()

    def test_change_delete_to_move_and_read(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.move_to_folder(Folder.NEWSLETTERS)
        change_filter.as_read()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_2_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_already_read(Folder.NEWSLETTERS, self.TEST_2_SUBJECT))
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.NEWSLETTERS, self.TEST_2_SUBJECT))

    def test_change_add_condition_and_send_notification(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_forward_to(self.TEST_3_SUBJECT, USEREMAIL_2 + '@mail.ru')

        change_filter = ChangeFilter(self.driver)
        condition_index = 1
        change_filter.change_filter_default(rule = Rule.size_KB, condition = '10000', index = condition_index, add = True)
        change_filter.forward_change_contex()
        change_filter.save(confirm_password = True)
        

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_3_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_3_SUBJECT))
        # TODO: check if itberries2@mail.ru get the letter #оно приходит, но надо проверять здесь
    
    def test_add_condition_and_revert_autoreply(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_copy_cond_and_autoreply(USEREMAIL_2)

        change_filter = ChangeFilter(self.driver)
        condition_index = 1
        change_filter.change_filter_default(rule = Rule.field_copy, condition = USEREMAIL_1, index = condition_index, add = True)
        change_filter.reply_switch()
        change_filter.switch_interaction_conditions()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_1 + '@mail.ru', subject = self.TEST_4_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_4_SUBJECT))

    def test_redirected_and_continue_filter(self):
        # Create filter in USERMAIL_2 that redirect letter with this subject back to USERMAIL1
        # And login back to main account
        
        change_filter = ChangeFilter(self.driver)
        change_filter.switch_mail_box(USEREMAIL_2)

        create_account2_filter = CreateFilter(self.driver)
        create_account2_filter.create_subject_cond_and_forward_to(self.TEST_5_SUBJECT, USEREMAIL_1 + '@mail.ru')

        log_out = LogOut(self.driver)
        log_out.log_out()

        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

        create_additional_filter = CreateFilter(self.driver)
        create_additional_filter.create_subject_cond_and_flag(self.TEST_5_SUBJECT)

        create_redirect_filter = CreateFilter(self.driver)
        create_redirect_filter.create_redirect_from_cond_and_continue(USEREMAIL_1)

        condition_index = 0
        change_filter.change_filter_default(rule = Rule.field_copy, condition = USEREMAIL_1, index = condition_index)
        change_filter.spam_on()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_2 + '@mail.ru', subject = self.TEST_5_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_have_flag(Folder.INBOX, self.TEST_5_SUBJECT))
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_5_SUBJECT))

        # delete filter in USERMAIL_2 account
        #log_out.log_out()