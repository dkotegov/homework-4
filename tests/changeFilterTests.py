# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter, LogOut
from tests.createFilter import CreateFilter
from tests.config import USEREMAIL_1, USEREMAIL_2

class ChangeFilterTest(unittest.TestCase):

    TEST_1_SUBJECT = 'Test 1 - Change MoveTo to Delete'
    TEST_2_SUBJECT = 'Test 2 - Change Delete to MoveTo'
    TEST_3_SUBJECT = 'Test 3 - Add cond Size and SendNotification'
    TEST_4_SUBJECT = 'Test 4 - Add cond Copy and revert AutoReply'
    TEST_5_SUBJECT = 'Test 5 - Redirected to'

    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1400, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

    def tearDown(self):
        self.driver.quit()
    
    # TODO: camel case style?
    # TESTS THAT WORK:
    def test_change_move_to_delete(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_to_cond_and_move_to_folter('Рассылки')

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.delete_message()
        change_filter.save_filter()
        
        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject(self.TEST_1_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_not_exists('Рассылки', self.TEST_1_SUBJECT), True)
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    def test_change_delete_to_move_and_read(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_delete(self.TEST_2_SUBJECT)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.move_to_folder('Рассылки')
        change_filter.as_read()
        change_filter.save_filter()
        
        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject(self.TEST_2_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_already_read('Рассылки', self.TEST_2_SUBJECT), True)
        self.assertEqual(check_filter_work.check_if_letter_exists_and_open_it('Рассылки', self.TEST_2_SUBJECT), True)
        check_filter_work.delete_letter(self.TEST_2_SUBJECT)
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    def test_change_add_condition_and_send_notification(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_subject_cond_and_forward_to(self.TEST_3_SUBJECT, 'itberries2@mail.ru')

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.add_condition()
        condition_index = 1
        change_filter.change_condition(Rule.size_KB, 1)
        change_filter.change_condition_value(condition_index, '10000')
        self.driver.execute_script("window.scrollTo(0, 200)") 
        change_filter.forward_change_contex()
        change_filter.save_filter()
        try:
            change_filter.confirm_password() # Need to confirm "forward to" operation with password (not all the time??)
        except:
            print("Password confirmation exception!") # little trick to confirm password
        
        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject(self.TEST_3_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check_if_letter_exists_and_open_it('Входящие', self.TEST_3_SUBJECT)
        check_filter_work.delete_letter(self.TEST_3_SUBJECT)
        # TODO: check if itberries2@mail.ru get the letter #оно приходит, но надо проверять здесь
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    
    def test_add_condition_and_revert_autoreply(self):
        create_filter = CreateFilter(self.driver)
        create_filter.create_copy_cond_and_autoreply('itberries2')

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.add_condition()
        condition_index = 1
        change_filter.change_condition(Rule.field_copy, condition_index)
        change_filter.change_condition_value(condition_index, 'it-berries')
        self.driver.execute_script("window.scrollTo(0, 200)") 
        change_filter.reply_switch()
        change_filter.switch_interaction_conditions()
        change_filter.save_filter()

        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject(self.TEST_4_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check_if_letter_exists_and_open_it('Входящие', self.TEST_4_SUBJECT)
        check_filter_work.delete_letter(self.TEST_4_SUBJECT)
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    def test_redirected_and_continue_filter(self):
        # Create filter in USERMAIL_2 that redirect letter with this subject back to USERMAIL1
        # And login back to main account
        log_out = LogOut(self.driver)
        log_out.log_out()
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_2)
        create_account2_filter = CreateFilter(self.driver)
        create_account2_filter.create_subject_cond_and_forward_to(self.TEST_5_SUBJECT, USEREMAIL_1 + '@mail.ru')
        log_out.log_out()
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_1)

        create_additional_filter = CreateFilter(self.driver)
        create_additional_filter.create_subject_cond_and_flag(self.TEST_5_SUBJECT)

        create_redirect_filter = CreateFilter(self.driver)
        create_redirect_filter.create_redirect_from_cond_and_continue(USEREMAIL_1)

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        condition_index = 0
        change_filter.change_condition(Rule.field_redirected_to, condition_index)
        change_filter.change_condition_value(condition_index, USEREMAIL_2)
        self.driver.execute_script("window.scrollTo(0, 200)") 
        change_filter.spam_on()
        change_filter.save_filter()

        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee(USEREMAIL_2 + '@mail.ru')
        write_letter.setSubject(self.TEST_5_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        self.assertEqual(check_filter_work.check_if_letter_have_flag('Входящие', self.TEST_5_SUBJECT), True)
        self.assertEqual(check_filter_work.check_if_letter_exists_and_open_it('Входящие', self.TEST_5_SUBJECT), True)
        check_filter_work.delete_letter(self.TEST_5_SUBJECT)
        check_filter_work.open_filters_page_in_new_window()

        # delete main and additional filters
        change_filter.delete_all()

        # delete filter in USERMAIL_2 account
        log_out.log_out()
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(USEREMAIL_2)
        create_account2_filter.delete_created_filter()
