from pages.MainPage import MainPage
from BasicTest import BasicTest

from user.User import User

import time

class MainTest(BasicTest):
  
  def setUp(self):
    super(MainTest, self).setUp()
    self.main_page = MainPage(self.driver)
    self.main_page.open()
    self.auth()
    self.main_page.hide_app_loader()
    
  # def check_first_letter(self, subject, text):
  #   actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
  #   actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
  #   self.assertEqual(subject, actual_subject)
  #   self.assertEqual(text, actual_text)
    
  # def test_receive_new_letter(self):
  #   subject = 'Subject_receive_new_letter'
  #   text = 'Text_receive_new_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.check_first_letter(subject, text)
    
  # def test_receive_new_letter_from_another_account(self):
  #   subject = 'Subj_receive_new_letter_from_another_account'
  #   text = 'Txt_receive_new_letter_from_another_account'
    
  #   receiver = User(self.login2, self.password2)
    
  #   self.main_page.letter_manager.write_letter(receiver.login, subject, text)
  #   self.main_page.relogin(receiver.login, receiver.password)
   
  #   self.check_first_letter(subject, text)
  
  # def test_unread_letter_status(self):
  #   subject = 'Subject_unread_letter_status'
  #   text = 'Text_unread_letter_status'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.assertFalse(self.main_page.letter_manager.letter_selector.get_first_letter_read_status())
    
  # def test_reading_letter(self):
  #   subject = 'Subject_reading_letter'
  #   text = 'Text_reading_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.main_page.letter_manager.letter_selector.set_first_letter_read_status(True)
  #   self.assertTrue(self.main_page.letter_manager.letter_selector.get_first_letter_read_status())
    
  # def test_remove_letter(self):
  #   subject = 'Subject_remove_letter'
  #   text = 'Text_remove_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.main_page.letter_manager.remove_first_letter()
    
  #   self.main_page.navigation_manager.go_to_trash()
  #   actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
  #   actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
  #   self.check_first_letter(subject, text)
    
  # def test_restore_letter(self):
  #   subject = 'Subject_restore_letter'
  #   text = 'Text_restore_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.main_page.letter_manager.remove_first_letter()
    
  #   self.main_page.navigation_manager.go_to_trash()
  #   self.main_page.letter_manager.restore_first_letter()
  #   # Go back (to check for a letter in the inbox folder)
  #   self.main_page.navigation_manager.go_to_inbox()
    
  #   self.check_first_letter(subject, text)
    
  # def test_check_sent_new_letter(self):
  #   subject = 'Subject_check_sent_new_letter'
  #   text = 'Text_check_sent_new_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.main_page.navigation_manager.go_to_sent_letters_folder()
  #   actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
  #   actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
  #   self.check_first_letter(subject, text)
  
  # def test_open_letter(self):
  #   subject = 'Subject_opened_letter'
  #   text = 'Text_opened_letter'
  #   self.main_page.letter_manager.write_letter(self.login, subject, text)
  #   self.main_page.letter_manager.letter_selector.open_first_letter()
  #   actual_subject = self.main_page.letter_manager.letter_selector.get_opened_letter_subject()
  #   actual_text = self.main_page.letter_manager.letter_selector.get_opened_letter_text()
  #   self.assertEqual(subject, actual_subject)
  #   self.assertEqual(text, actual_text)
    
  # def test_reply_letter(self):
  #   subject = 'Subject_reply_letter'
  #   text = 'Text_reply_letter' 
  #   replied_text = 'Replied text'
    
  #   first_user = User(self.login, self.password)
  #   receiver = User(self.login2, self.password2)
    
  #   self.main_page.letter_manager.write_letter(receiver.login, subject, text)
    
  #   self.main_page.relogin(receiver.login, receiver.password)
  #   self.main_page.letter_manager.reply_letter(replied_text)

  #   self.main_page.relogin(first_user.login, first_user.password)
  #   self.main_page.letter_manager.letter_selector.open_first_letter()
  #   actual_replied_text = self.main_page.letter_manager.letter_selector.get_replied_letter_text()
  #   self.assertEqual(replied_text, actual_replied_text)
    
  # def test_write_many_receivers(self):
  #   subject = 'Subject_write_many_receivers'
  #   text = 'Text_write_many_receivers'
  #   receivers = [
  #     User(self.login, self.password),
  #     User(self.login2, self.password2),
  #   ]
  #   receivers_emails = [receiver.login for receiver in receivers]
  #   self.main_page.letter_manager.write_letter_many_receivers(receivers_emails, subject, text)
  #   for receiver in receivers:
  #     self.main_page.relogin(receiver.login, receiver.password)
  #     self.check_first_letter(subject, text)
    
  def test_bold_letter(self):
      subject = 'Subject_bold_letter'
      text = 'Text_bold_letter' 
      self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
      self.main_page.letter_manager.letter_writer.set_bold_text()
      self.main_page.letter_manager.send_letter()
      self.main_page.letter_manager.letter_selector.open_first_letter()
      
      bold_element = self.main_page.letter_manager.letter_selector.get_bold()
      self.assertEqual(text, bold_element.text)
      
  def test_font_title1_letter(self):
    subject = 'Subject_font_title1_letter_letter'
    text = 'font title1 letter' 
    self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
    self.main_page.letter_manager.letter_writer.set_font_text_title1()
    
    
    self.main_page.letter_manager.send_letter()
    self.main_page.letter_manager.letter_selector.open_first_letter()
    element = self.main_page.letter_manager.letter_selector.get_font_text_title1()
    style = 'font-size: 32px; line-height: 40px;'
    self.assertEqual(style, element.get_attribute('style').encode('utf-8', errors='ignore'))
      
  def test_italic_letter(self):
    subject = 'Subject_italic_letter'
    text = 'Text_italic_letter' 
    self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
    self.main_page.letter_manager.letter_writer.set_italic_text()
    self.main_page.letter_manager.send_letter()
    self.main_page.letter_manager.letter_selector.open_first_letter()
      
    italic_element = self.main_page.letter_manager.letter_selector.get_italic()
    self.assertEqual(text, italic_element.text)
      
  def test_underline_letter(self):
    subject = 'Subject_underline_letter'
    text = 'Text_underline_letter' 
    self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
    self.main_page.letter_manager.letter_writer.set_underline_text()
    self.main_page.letter_manager.send_letter()
    self.main_page.letter_manager.letter_selector.open_first_letter()
      
    underline_element = self.main_page.letter_manager.letter_selector.get_underline()
    self.assertEqual(text, underline_element.text)
    
  def test_strike_through_letter(self):
    subject = 'Subject_strike_through_letter'
    text = 'Text_strike_through_letter' 
    self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
    self.main_page.letter_manager.letter_writer.set_strike_through_text()
    self.main_page.letter_manager.send_letter()
    self.main_page.letter_manager.letter_selector.open_first_letter()
      
    strike_through_element = self.main_page.letter_manager.letter_selector.get_strike_through()
    self.assertEqual(text, strike_through_element.text)
  
  # def test_text_color(self):
  #   subject = 'Subject_text_color'
  #   text = 'Text_color' 
  #   self.main_page.letter_manager.write_letter_without_sending(self.login, subject, text)
  #   self.main_page.letter_manager.letter_writer.set_text_color_purple()
  #   self.main_page.letter_manager.send_letter()
  #   self.main_page.letter_manager.letter_selector.open_first_letter()
  #   element = self.main_page.letter_manager.letter_selector.get_text_color_purple()
  #   self.assertEqual(text, element.text)
  #   style = 'color:#e70091;'
  #   self.assertEqual(style, element.get_attribute('style').encode('utf-8', errors='ignore'))
      
      
    
