from pages.MainPage import MainPage
from BasicTest import BasicTest
import time

class MainTest(BasicTest):
  
  def pre_tests(self):
    self.main_page = MainPage(self.driver)
    self.main_page.open()
    self.auth()
    
  def test_receive_new_letter(self):
    subject = 'Subject_1'
    text = 'Text1'
    self.main_page.write_letter(self.login, subject, text)
    actual_subject = self.main_page.get_first_letter_subject()
    actual_text = self.main_page.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_unread_letter_status(self):
    self.main_page.write_letter('TPWAO@mail.ru', 'Subject 2', 'Text 2')
    self.assertFalse(self.main_page.get_first_letter_read_status())
    
  def test_reading_letter(self):
    self.main_page.write_letter('TPWAO@mail.ru', 'Subject 3', 'Text 3')
    self.main_page.set_first_letter_read_status(True)
    self.assertTrue(self.main_page.get_first_letter_read_status())
    
  def test_unreading_letter(self):
    self.main_page.write_letter('TPWAO@mail.ru', 'Subject4', 'Text4')
    self.main_page.set_first_letter_read_status(True)
    self.main_page.set_first_letter_read_status(False)
    self.assertFalse(self.main_page.get_first_letter_read_status())

  def test_remove_letter(self):
    subject = 'Subject 5'
    text = 'Text 5'
    self.main_page.write_letter('TPWAO@mail.ru', subject, text)
    self.main_page.remove_first_letter()
    
    self.main_page.click_nav_trash_button()
    actual_subject = self.main_page.get_first_letter_subject()
    actual_text = self.main_page.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_restore_letter(self):
    subject = 'Subject 6'
    text = 'Text 6'
    self.main_page.write_letter('TPWAO@mail.ru', subject, text)
    self.main_page.remove_first_letter()
    
    self.main_page.click_nav_trash_button()
    self.main_page.restore_first_letter()
    # Go back (to check for a letter in the inbox folder)
    self.main_page.click_nav_inbox_button()
    actual_subject = self.main_page.get_first_letter_subject()
    actual_text = self.main_page.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_remove_all_letters_from_inbox(self):
    for i in range(2):
      self.main_page.write_letter('TPWAO@mail.ru', 'Subject7%d' % i, 'Text7%d' % i)
    self.main_page.move_all_letters_to_trash()
    self.main_page.is_there_no_letters()
    
  def test_restore_all_letters_to_inbox(self):
    for i in range(2):
      self.main_page.write_letter('TPWAO@mail.ru', 'Subject8%d' % i, 'Text8%d' % i)
      
    self.main_page.move_all_letters_to_trash()
    self.main_page.click_nav_trash_button()
    self.main_page.restore_all_letters_from_trash()
    self.main_page.is_there_no_letters()
    
  def test_clean_trash(self):
    for i in range(2):
      self.main_page.write_letter('TPWAO@mail.ru', 'Subject9%d' % i, 'Text9%d' % i)
      
    self.main_page.move_all_letters_to_trash()
    self.main_page.click_nav_trash_button()
    self.main_page.clean_trash()
    self.main_page.is_there_no_letters()
    
    