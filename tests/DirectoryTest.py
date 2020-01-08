from BasicTest import BasicTest
from pages.DirectoryPage import DirectoryPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from config import config

import time

class DirectoryTest(BasicTest):
    SETTINGS_NOTIFICATIONS_URL = 'https://e.mail.ru/settings/notifications'
    ARCHIVE_URL = 'https://e.mail.ru/archive'
    MAIN_URL = 'https://e.mail.ru'

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
        letter_subject = 'Archive mail'
        letter_text = 'Lorem text for archive'
        main_page.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        main_page.click_letter_avatar()    
        self.directory_page.move_to_archive()

        main_page.get_first_letter()

        self.assertEqual(letter_subject, main_page.get_first_letter_subject())
        self.assertEqual(letter_text, main_page.get_first_letter_text())



    
    
        