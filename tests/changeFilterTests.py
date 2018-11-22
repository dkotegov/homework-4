# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter
from tests.createFilter import CreateFilter

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
        open_filter_settings.open()

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
        check_filter_work.check_if_letter_not_exists('Рассылки', self.TEST_1_SUBJECT)
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
        check_filter_work.check_if_letter_exists_and_open_it('Рассылки', self.TEST_2_SUBJECT)
        #TODO: check that letter is read
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()
'''
    def test_change_add_condition_and_send_notification(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_subject, condition_index)
        create_new_filter.change_condition_value(condition_index, 'Test')
        create_new_filter.show_other_actions()
        create_new_filter.forward_to('itberries2@mail.ru')
        create_new_filter.save_filter()
        try:
            create_new_filter.confirm_password() # Need to confirm "forward to" operation with password (not all the time??)
        except:
            print("Password confirmation exception!") # little trick to confirm password

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
        # TODO: check if itberries2@mail.ru get the letter #оно приходит, но надо проверять здесь
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    def test_add_condition_and_revert_autoreply(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_copy, condition_index)
        create_new_filter.change_condition_effect(condition_index)
        create_new_filter.change_condition_value(condition_index, 'itberries2')
        create_new_filter.show_other_actions()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        create_new_filter.reply_not_found()
        create_new_filter.save_filter()

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
        check_filter_work.open_filters_page_in_new_window()

        change_filter.delete()

    def test_redirected_and_continue_filter(self):
        # There is filter in itberries2@mail.ru that redirect letter with this subject back to it-berries@mail.ru

        create_additional_filter = CreateNewFilter(self.driver)
        create_additional_filter.open()
        condition_index = 0
        create_additional_filter.change_condition(Rule.field_subject, condition_index)
        create_additional_filter.change_condition_value(condition_index, self.TEST_5_SUBJECT)
        create_additional_filter.action_flag()
        create_additional_filter.save_filter()

        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_redirected_from, condition_index)
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        create_new_filter.show_other_actions()
        self.driver.execute_script("window.scrollTo(0, 200)") 
        create_new_filter.continue_to_filter()
        create_new_filter.save_filter()

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        condition_index = 0
        change_filter.change_condition(Rule.field_redirected_to, condition_index)
        change_filter.change_condition_value(condition_index, 'itberries2')
        self.driver.execute_script("window.scrollTo(0, 200)") 
        change_filter.spam_on()
        change_filter.save_filter()

        change_filter.check_if_filter_list_exists()
        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('itberries2@mail.ru')
        write_letter.setSubject(self.TEST_5_SUBJECT)
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check_if_letter_exists_and_open_it('Входящие', self.TEST_5_SUBJECT)
        #TODO: check that additional filter works (check that letter has red flag)
        check_filter_work.delete_letter(self.TEST_5_SUBJECT)
        check_filter_work.open_filters_page_in_new_window()

        # delete main and additional filters
        change_filter.delete()
        # change_filter.delete() # TODO: can not delete second time (additional filter): Element is not interactable

'''