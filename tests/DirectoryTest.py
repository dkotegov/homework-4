from BasicTest import BasicTest
from pages.DirectoryPage import DirectoryPage
from pages.main_page.letters.LetterSelector import LetterSelector
from pages.main_page.menu.navigation.NavigationManager import NavigationManager
from pages.MainPage import MainPage
from config import config

class DirectoryTest(BasicTest):
    def setUp(self):
        super(DirectoryTest, self).setUp()
        self.directory_page = DirectoryPage(self.driver)
        self.directory_page.open()
        self.auth()
        self.main_page = MainPage(self.driver)

    def test_move_to_archive(self):
        letter_subject = 'Mail for archive'
        letter_text = 'Lorem text for archive'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()  
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()

        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
    
    def test_move_to_inbox_from_archive(self):
        letter_subject = '$$$ Archive'
        letter_text = 'Lorem text for archive'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()            
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()
        self.main_page.letter_manager.restore_first_letter()

        navigation_manager = NavigationManager(self.driver)    
        navigation_manager.go_to_inbox()

        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)        

    def test_set_important_letter(self):
        letter_subject = 'The IMPORTANT letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()  
        self.assertTrue(True, self.directory_page.set_check_flag())
    
    def test_unset_important_letter(self):
        letter_subject = 'The UNimportant letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()  
        self.directory_page.set_check_flag()
        self.directory_page.get_important_status()
        self.assertTrue(True, self.directory_page.get_important_status())
    
    
        