from pages.MainPage import MainPage
from BasicTest import BasicTest
import time

class MainTest(BasicTest):
  
  def setUp(self):
    super(MainTest, self).setUp()
    self.main_page = MainPage(self.driver)
    self.main_page.open()
    self.auth()
    self.main_page.hide_app_loader()
    
  def test_receive_new_letter(self):
    subject = 'Subject_receive_new_letter'
    text = 'Text_receive_new_letter'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
    actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_unread_letter_status(self):
    subject = 'Subject_unread_letter_status'
    text = 'Text_unread_letter_status'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    self.assertFalse(self.main_page.letter_manager.letter_selector.get_first_letter_read_status())
    
  def test_reading_letter(self):
    subject = 'Subject_reading_letter'
    text = 'Text_reading_letter'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    self.main_page.letter_manager.letter_selector.set_first_letter_read_status(True)
    self.assertTrue(self.main_page.letter_manager.letter_selector.get_first_letter_read_status())
    
  def test_remove_letter(self):
    subject = 'Subject_remove_letter'
    text = 'Text_remove_letter'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    self.main_page.letter_manager.remove_first_letter()
    
    self.main_page.navigation_manager.go_to_trash()
    actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
    actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_restore_letter(self):
    subject = 'Subject_restore_letter'
    text = 'Text_restore_letter'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    self.main_page.letter_manager.remove_first_letter()
    
    self.main_page.navigation_manager.go_to_trash()
    self.main_page.letter_manager.restore_first_letter()
    # Go back (to check for a letter in the inbox folder)
    self.main_page.navigation_manager.go_to_inbox()
    
    actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
    actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_remove_all_letters_from_inbox(self):
    for i in range(2):
      subject = 'Subject_remove_all_letters_from_inbox%d'
      text = 'Text_remove_all_letters_from_inbox%d'
      self.main_page.letter_manager.write_letter(self.login, subject % i, text % i)
    self.main_page.letter_manager.move_all_letters_to_trash()
    self.main_page.letter_manager.letter_selector.is_there_no_letters()
    
  def test_restore_all_letters_to_inbox(self):
    for i in range(2):
      subject = 'Subject_restore_all_letters_to_inbox%d'
      text = 'Text_restore_all_letters_to_inbox%d'
      self.main_page.letter_manager.write_letter(self.login, subject % i, text % i)
      
    self.main_page.letter_manager.move_all_letters_to_trash()
    self.main_page.navigation_manager.go_to_trash()
    self.main_page.letter_manager.restore_all_letters_from_trash()
    self.main_page.letter_manager.letter_selector.is_there_no_letters()
    
  def test_clean_trash(self):
    for i in range(2):
      subject = 'Subject_clean_trash%d'
      text = 'Text_clean_trash%d'
      self.main_page.letter_manager.write_letter(self.login, subject % i, text % i)
      
    self.main_page.letter_manager.move_all_letters_to_trash()
    self.main_page.navigation_manager.go_to_trash()
    self.main_page.trash_cleaner.clean()
    self.main_page.letter_manager.letter_selector.is_there_no_letters()
    
  def test_check_sent_new_letter(self):
    subject = 'Subject_check_sent_new_letter'
    text = 'Text_check_sent_new_letter'
    self.main_page.letter_manager.write_letter(self.login, subject, text)
    self.main_page.navigation_manager.go_to_sent_letters_folder()
    actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
    actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    