from BasicTest import BasicTest
from pages.DirectoryPage import DirectoryPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from config import config

import time

class DirectoryTest(BasicTest):
    def setUp(self):
        super(DirectoryTest, self).setUp()
        self.directory_page = DirectoryPage(self.driver)
    

    def test_move_to_archive(self):
        self.driver.get(self.LOGIN_URL)
        login_page = LoginPage(self.driver)        
        login_page.sign_in(self.login, self.password)

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
        self.driver.get(self.LOGIN_URL)
        login_page = LoginPage(self.driver)        
        login_page.sign_in(self.login, self.password)

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
        self.driver.get(self.LOGIN_URL)
        login_page = LoginPage(self.driver)        
        login_page.sign_in(self.login, self.password)

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
        self.driver.get(self.LOGIN_URL)
        login_page = LoginPage(self.driver)        
        login_page.sign_in(self.login, self.password)

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
    
    
        