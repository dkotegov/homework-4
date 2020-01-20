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
        self.assertTrue( self.directory_page.set_check_flag())
    
    def test_unset_important_letter(self):
        letter_subject = 'The UNimportant letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()  
        self.directory_page.set_check_flag()
        self.directory_page.get_important_status()
        self.assertFalse(False, self.directory_page.get_important_status())

    def test_move_to_social(self):
        letter_subject = 'The SOCIAL letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()

        self.directory_page.move_to_social()
        self.directory_page.go_to_social()

        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
    
    def test_move_to_inbox_from_social(self):
        letter_subject = 'not SOCIAL letter'
        letter_text = 'Lorem text for archive'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()

        self.directory_page.move_to_social()
        self.directory_page.go_to_social()
        self.main_page.letter_manager.restore_first_letter()

        navigation_manager = NavigationManager(self.driver)    
        navigation_manager.go_to_inbox()
        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)

    def test_move_to_newsletters(self):
        letter_subject = 'The NewsLetter letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()

        self.directory_page.move_to_newsletters()
        self.directory_page.go_to_newsletters()

        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
    
    def test_move_to_inbox_from_newsletters(self):
        letter_subject = 'The NewsLetter letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.write_letter(config.DEFAULT_MAIL, letter_subject, letter_text)
        self.main_page.letter_manager.letter_selector.select_first_letter()

        self.directory_page.move_to_newsletters()
        self.directory_page.go_to_newsletters()
        self.main_page.letter_manager.restore_first_letter()

        navigation_manager = NavigationManager(self.driver)    
        navigation_manager.go_to_inbox()
        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
    
    def test_send_empty_letter(self):
        self.main_page.letter_manager.letter_writer.click_write_letter_button()
        self.main_page.letter_manager.letter_writer.click_send_letter_button()
        self.assertTrue( self.directory_page.check_error_message())

    def test_send_letter_without_subject(self):
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.letter_writer.click_write_letter_button()
        self.main_page.letter_manager.letter_writer.enter_email_receiver(config.DEFAULT_MAIL)
        self.main_page.letter_manager.letter_writer.enter_textbox(letter_text)
        self.main_page.letter_manager.letter_writer.click_send_letter_button()
        self.main_page.letter_manager.letter_writer.close_sent_window()
        
        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        empty_subject = self.directory_page.empty_subject_text
        self.assertEqual(empty_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)  

    def test_send_letter_without_receiver(self):
        letter_subject = 'Subject letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.letter_writer.click_write_letter_button()
        self.main_page.letter_manager.letter_writer.enter_subject(letter_subject)
        self.main_page.letter_manager.letter_writer.enter_textbox(letter_text)
        self.main_page.letter_manager.letter_writer.click_send_letter_button()
        self.assertTrue( self.directory_page.check_error_message())

    def test_save_draft_letter(self):
        letter_subject = 'Draft letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.letter_writer.click_write_letter_button()
        self.main_page.letter_manager.letter_writer.enter_subject(letter_subject)
        self.main_page.letter_manager.letter_writer.enter_textbox(letter_text)
        self.directory_page.click_save_mail()

        self.directory_page.close_writer_window()
  
        self.directory_page.go_to_drafts()
   
        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
    
    def test_save_draft_letter(self):
        letter_subject = 'Send draft letter'
        letter_text = 'Lorem text lorem lorem lorem'
        self.main_page.letter_manager.letter_writer.click_write_letter_button()
        self.main_page.letter_manager.letter_writer.enter_email_receiver(config.DEFAULT_MAIL)
        self.main_page.letter_manager.letter_writer.enter_subject(letter_subject)
        self.main_page.letter_manager.letter_writer.enter_textbox(letter_text)
        self.directory_page.click_save_mail()
        self.directory_page.close_writer_window()
        self.directory_page.go_to_drafts()
        self.directory_page.open_draft()
        self.main_page.letter_manager.letter_writer.click_send_letter_button()
        self.main_page.letter_manager.letter_writer.close_sent_window()

        navigation_manager = NavigationManager(self.driver)    
        navigation_manager.go_to_inbox()

        letter_selector = LetterSelector(self.driver)
        actual_subject = letter_selector.get_first_letter_subject()
        actual_text = letter_selector.get_first_letter_text()
        self.main_page.letter_manager.remove_first_letter()
        self.assertEqual(letter_subject, actual_subject)
        self.assertEqual(letter_text, actual_text)
        