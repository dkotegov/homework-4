# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from steps.steps import OpenFilterSettings, CreateNewFilter, Rule, WriteLetter, CheckFilterWork, ChangeFilter

class ChangeFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
		    command_executor='http://127.0.0.1:4444/wd/hub',
	        desired_capabilities=DesiredCapabilities.CHROME )
        self.driver.set_window_size(1400, 1080)
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open()

    def tearDown(self):
        self.driver.quit()

    # I DON'T CHECK THIS TEST:
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
            print("No password confirmation exception!") # little trick to confirm password

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
            print("No password confirmation exception!") # little trick to confirm password
        change_filter.check_if_filter_list_exists()

        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject('Test - Добавить условие размера и переслать уведомление')
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check('Входящие', 'Test - Добавить условие размера и переслать уведомление')
        # TODO: check if itberries2@mail.ru get the letter
        change_filter.delete()

    #TODO: create tests functions

'''
    # TEST THAT WORK:
    def test_change_move_to_delete(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        create_new_filter.move_to_folder('Рассылки')
        create_new_filter.save_filter()

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.delete_message()
        change_filter.save_filter()
        change_filter.check_if_filter_list_exists()

        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject('Test - Замена Поместить в папку на Удалить')
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check_if_letter_not_exists('Рассылки', 'Test - Замена Поместить в папку на Удалить')

        change_filter.delete()

    def test_change_delete_to_move_and_read(self):
        create_new_filter = CreateNewFilter(self.driver)
        create_new_filter.open()
        condition_index = 0
        create_new_filter.change_condition(Rule.field_from, condition_index)
        create_new_filter.change_condition_value(condition_index, 'it-berries')
        create_new_filter.delete_message()
        create_new_filter.save_filter()

        change_filter = ChangeFilter(self.driver)
        change_filter.open()
        change_filter.move_to_folder('Рассылки')
        change_filter.as_read()
        change_filter.save_filter()
        change_filter.check_if_filter_list_exists()

        write_letter = WriteLetter(self.driver)
        write_letter.open()
        write_letter.setAddressee('it-berries@mail.ru')
        write_letter.setSubject('Test - Замена Удалить на Поместить в папку')
        write_letter.send()

        check_filter_work = CheckFilterWork(self.driver)
        check_filter_work.check('Рассылки', 'Test - Замена Удалить на Поместить в папку')
        #TODO: check that letter is read

        change_filter.delete()
'''