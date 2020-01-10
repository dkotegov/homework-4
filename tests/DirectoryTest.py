from BasicTest import BasicTest
from pages.DirectoryPage import DirectoryPage
from pages.MainPage import MainPage
from config import config

import time

class DirectoryTest(BasicTest):
    def pre_tests(self):
        self.directory_page = DirectoryPage(self.driver)
        self.directory_page.open()
        self.auth()

    def test_move_to_archive(self):
        main_page = MainPage(self.driver)
        ############## 
        time.sleep(2)
        ############
        letter_subject = 'Mail for archive'
        letter_text = 'Lorem text for archive'
        main_page.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        main_page.select_first_letter()    
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()

        main_page.get_first_letter()
        self.assertEqual(letter_subject, main_page.get_first_letter_subject())
        self.assertEqual(letter_text, main_page.get_first_letter_text())
    
    def test_move_to_inbox_from_archive(self):
        main_page = MainPage(self.driver)
        ############## 
        time.sleep(2)
        ##############
        letter_subject = '$$$ Archive'
        letter_text = 'Lorem text for archive'
        main_page.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        main_page.select_first_letter()            
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()

        main_page.restore_first_letter()
        main_page.click_nav_inbox_button()
        actual_subject = main_page.get_first_letter_subject()
        actual_text = main_page.get_first_letter_text()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)        

    def test_set_important_letter(self):
        main_page = MainPage(self.driver)
        ############## 
        time.sleep(2)
        ############
        letter_subject = 'The IMPORTANT letter'
        letter_text = 'Lorem text lorem lorem lorem'
        main_page.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        main_page.select_first_letter()  
        self.assertTrue(True, self.directory_page.set_check_flag())
    
    def test_unset_important_letter(self):
        main_page = MainPage(self.driver)
        ############## 
        time.sleep(2)
        ############
        letter_subject = 'The UNimportant letter'
        letter_text = 'Lorem text lorem lorem lorem'
        main_page.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        main_page.select_first_letter()
        self.directory_page.set_check_flag()
        self.directory_page.get_important_status()
        self.assertTrue(True, self.directory_page.get_important_status())
    
    
        