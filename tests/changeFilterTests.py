# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter, LogOut, Cleaner
from support.folders import Folder
from tests.createFilter import CreateFilter
from tests.config import USEREMAIL_1, USEREMAIL_2, HUB_ADDRESS, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, USEREMAIL_FULL_1, USEREMAIL_FULL_2

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
        self.is_used_second_mail = False
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        # delete filters and letters in two mail accounts

        create_filter = CreateFilter(self.driver)
        cleaner = Cleaner(self.driver)
        check_filter_work = CheckFilterWork(self.driver)
        cleaner.delete_all_letters()
        check_filter_work.open_filters_page_in_new_window()
        create_filter.delete_created_filter()
        if self.is_used_second_mail is True:
            create_new_filter = CreateNewFilter(self.driver)
            create_new_filter.switch_mail_box(USEREMAIL_2)
            create_new_filter.delete_all()
            cleaner.delete_all_letters()
        self.driver.quit()
    
    
    def test_change_move_to_delete(self):
        # create a filter that move letters 
        # and change it to delete
        
        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter(Folder.NEWSLETTERS)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.delete_message()
        change_filter.save()

        check_filter_work = CheckFilterWork(self.driver)
        was_num_of_letters = check_filter_work.get_number_of_letters()
        print('number was get and it is: ')
        print(was_num_of_letters)

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_FULL_1, subject = self.TEST_1_SUBJECT)

        self.assertTrue(check_filter_work.check_if_letter_not_exists(Folder.NEWSLETTERS, was_num_of_letters))

    '''
    def test_change_delete_to_move_and_read(self):
        # create a filter that deletes messages 
        # and change it to move and set as read

        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.move_to_folder(Folder.NEWSLETTERS)
        change_filter.as_read()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_FULL_1, subject = self.TEST_2_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_already_read(Folder.NEWSLETTERS, self.TEST_2_SUBJECT))
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.NEWSLETTERS, self.TEST_2_SUBJECT))
    

    def test_change_add_condition_and_send_notification(self):
        # create a filter that forwards letters to mail2 
        # and change it with new condition and notification

        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_forward_to(self.TEST_3_SUBJECT, USEREMAIL_FULL_2)

        change_filter = ChangeFilter(self.driver)
        condition_index = 1
        change_filter.change_filter_default(rule = Rule.size_KB, condition = '10000', index = condition_index, add = True)
        change_filter.forward_change_contex()
        change_filter.save(confirm_password = False)

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_FULL_1, subject = self.TEST_3_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_3_SUBJECT))
        
        # check if email2 get the notification letter
        change_filter.switch_mail_box(USEREMAIL_2)
        self.is_used_second_mail = True
        write_letter.open() # go to old view of mail.ru inbox
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, 'Novaja pochta v it-berries@mail.ru'))
        change_filter.switch_mail_box(USEREMAIL_1)

    
    def test_add_condition_and_revert_autoreply(self):
        # create a filter with copy condition and autoreply 
        # and change it with new condition and revert autoreply

        create_filter = CreateFilter(self.driver)
        create_filter.create_copy_cond_and_autoreply(USEREMAIL_2)

        change_filter = ChangeFilter(self.driver)
        condition_index = 1
        change_filter.change_filter_default(rule = Rule.field_copy, condition = USEREMAIL_1, index = condition_index, add = True)
        change_filter.reply_switch()
        change_filter.switch_interaction_conditions()
        change_filter.save()

        write_letter = WriteLetter(self.driver)
        write_letter.send_letter(addressee = USEREMAIL_FULL_1, subject = self.TEST_4_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_4_SUBJECT))

    def test_redirected_and_continue_filter(self):
        # create three filters (email1: additional with flag, redirect; email2: forward to email1)
        # and change redirect filter to continue and add spam on
        
        # create filter in USERMAIL_2 that redirect letter with this subject back to USERMAIL1
        # And login back to main account
        change_filter = ChangeFilter(self.driver)
        change_filter.switch_mail_box(USEREMAIL_2)
        self.is_used_second_mail = True

        create_account2_filter = CreateFilter(self.driver)
        create_account2_filter.create_subject_cond_and_forward_to(self.TEST_5_SUBJECT, USEREMAIL_FULL_1)

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
        write_letter.send_letter(addressee = USEREMAIL_FULL_2, subject = self.TEST_5_SUBJECT)

        check_filter_work = CheckFilterWork(self.driver)
        self.assertTrue(check_filter_work.check_if_letter_have_flag(Folder.INBOX, self.TEST_5_SUBJECT))
        self.assertTrue(check_filter_work.check_if_letter_exists_and_open_it(Folder.INBOX, self.TEST_5_SUBJECT))
    '''